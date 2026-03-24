# %% Imports
import geopandas as gpd
import pandas as pd
import os
import glob
import sqlite3
import matplotlib.pyplot as plt
# %% Path and sensor names
db_path = "/Users/kylenessen/Library/CloudStorage/OneDrive-Althouse&Meade,Inc/Masters/WindLog"

sensors = ['FireSong', 'DotSpace', 'TechCore', 'WingSpan', 'LeafWind', 'WindFury',
           'PureWave', 'GlowWire', 'BeeSwarm', 'RoseKiss', 'DiveDeep', 'LightRay']
# %% Get SQLite files and build df

# Get all SQLite files in the directory
sqlite_files = glob.glob(os.path.join(db_path, "*.s3db"))

# Initialize an empty list to hold DataFrames
dfs = []

# For each SQLite file
for sqlite_file in sqlite_files:
    # Extract the sensor name from the file name
    sensor_name = os.path.basename(sqlite_file).split('.')[0]

    # If the sensor name is in the list of sensors we're interested in
    if sensor_name in sensors:
        # Connect to the SQLite database
        conn = sqlite3.connect(sqlite_file)

        # Use pd.read_sql_query to read the "Wind" table into a DataFrame
        df = pd.read_sql_query("SELECT * FROM Wind", conn)

        # Add a new column to the DataFrame that contains the sensor name
        df['Sensor'] = sensor_name

        # Append the DataFrame to the list
        dfs.append(df)

# Concatenate all DataFrames in the list into a single DataFrame
df = pd.concat(dfs, ignore_index=True)
# %% Remove non-recording days
df['speed'] = pd.to_numeric(df['speed'], errors='coerce')
df['speed_mph'] = df['speed'] * 2.23694

# Convert 'time' to datetime
df['time'] = pd.to_datetime(df['time'])

# Extract date from 'time'
df['date'] = df['time'].dt.date
# Convert 'gust' to numeric
df['gust'] = pd.to_numeric(df['gust'], errors='coerce')

# Group by 'date' and 'Sensor', calculate mean of 'gust'
gust_means = df.groupby(['date', 'Sensor'])['gust'].mean()

# Filter out dates where mean 'gust' is 0
valid_dates_sensors = gust_means[gust_means != 0].reset_index()[
    ['date', 'Sensor']]

# Filter original DataFrame
df = df.merge(valid_dates_sensors, how='inner', on=['date', 'Sensor'])
# %% Build categorical columns for wind speeds
df['5mph'] = df['speed_mph'].apply(lambda x: 1 if x >= 5 else 0)
df['9mph'] = df['speed_mph'].apply(lambda x: 1 if x >= 9 else 0)
# %% Make pivot table
pivot_table = df.pivot_table(
    values=['5mph', '9mph'], index='Sensor', aggfunc='mean')
# Multiply each column by 100 and round to the nearest tenth
pivot_table = (pivot_table * 100).round(1)


# %% Read in sensor locations

sensor_location_path = "/Users/kylenessen/Documents/Code/masters/pismo_monarch_grove/wind_meters.gpkg"

# Read the file into a GeoDataFrame
gdf = gpd.read_file(sensor_location_path)

# Convert 'height_m' to 'height_ft'
gdf['height_ft'] = gdf['height_m'] * 3.281
# %% Join sensor height to df
# Merge 'height_ft' from 'gdf' to 'df'
df = df.merge(gdf[['sensor_name', 'height_ft']],
              left_on='Sensor', right_on='sensor_name', how='left')

# Drop the 'sensor_name' column as it's duplicate
df = df.drop(columns='sensor_name')


# %% Read in weatherUnderground wind data
wu_path = "/Users/kylenessen/Downloads/weather_underground_observations.db 4"
# Create a connection to the SQLite database
conn = sqlite3.connect(wu_path)

# Query all records in the database
wu = pd.read_sql_query("SELECT * FROM weather_data", conn)

# Don't forget to close the connection
conn.close()
# %%
wu['speed_mph'] = wu['windSpeed'] * 2.23694
wu['5mph'] = wu['speed_mph'].apply(lambda x: 1 if x >= 5 else 0)
wu['9mph'] = wu['speed_mph'].apply(lambda x: 1 if x >= 9 else 0)
# %% Filter to relevant stations
stations = ['KCAGROVE128', 'KCAGROVE94', 'KCAGROVE99']
# Filter 'wu' to just the stations in 'stations'
wu = wu[wu['stationID'].isin(stations)]
# %%
wu_pivot_table = wu.pivot_table(
    values=['5mph', '9mph'], index='stationID', aggfunc='mean')
# Multiply each column by 100 and round to the nearest tenth
wu_pivot_table = (wu_pivot_table * 100).round(1)
# %%
# Concatenate 'pivot_table' and 'wu_pivot_table'
pivot_table = pd.concat([pivot_table, wu_pivot_table], ignore_index=False)
# %% Plot the data as a bar chart for '5mph' and '9mph' observations
pivot_table[['5mph', '9mph']].plot(kind='bar', figsize=(20, 12))
# Adjust y-axis scale
plt.ylim(0, 50)
# Add red line
plt.axhline(y=5, color='r', linestyle='--')
plt.rcParams['font.size'] = 14
plt.tick_params(axis='both', which='major', labelsize=14)
plt.title(
    'Two months of wind observations at Pismo Monarch Grove (Oct 11 - Dec 12, 2023)')
plt.xlabel('Sensor Name')
plt.ylabel('Percent of Observations')
# Show the plot
plt.show()
# %%
