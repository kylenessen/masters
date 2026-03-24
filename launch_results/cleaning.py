# %%
import pandas as pd
from datetime import datetime
import pytz

df2023 = pd.read_csv('2023_raw.csv')
df2024 = pd.read_csv('2024_raw.csv')
# %%


def clean_spacex_data(df):
    # Create a new empty dataframe to store cleaned data
    cleaned_df = pd.DataFrame(columns=df.columns)

    i = 0
    while i < len(df):
        current_row = df.iloc[i]

        # Check if this is a launch row (contains date and other details)
        if pd.notna(current_row[1]) and isinstance(current_row[1], str) and "202" in current_row[1]:
            # If next row exists and is a description row
            if i + 1 < len(df):
                description = df.iloc[i + 1][1]
                current_row['Description'] = description
                i += 2
            else:
                current_row['Description'] = ''
                i += 1
        else:
            i += 1
            continue

        cleaned_df = pd.concat(
            [cleaned_df, current_row.to_frame().T], ignore_index=True)

    # Split columns with newline characters
    # Date and time
    cleaned_df[['Date', 'Time (UTC)']] = cleaned_df['Date and\ntime (UTC)'].str.split(
        '\n', expand=True)

    # Version and booster
    cleaned_df[['Version', 'Booster ID']
               ] = cleaned_df['Version,\nbooster'].str.split('\n', expand=True)

    # Launch site
    cleaned_df[['Launch Site', 'Pad']
               ] = cleaned_df['Launch\nsite'].str.split(',', expand=True)

    # Launch outcome and Booster landing
    cleaned_df = cleaned_df.rename(columns={
        'Launch\noutcome': 'Launch Outcome',
        'Booster\nlanding': 'Booster Landing'
    })

    # Handle landing outcome and site
    # First, extract the landing site
    cleaned_df['Landing Location'] = cleaned_df['Booster Landing'].str.extract(
        r'\((.*?)\)')
    # Then, get just the outcome part by taking everything before the first parenthesis
    cleaned_df['Booster Landing'] = cleaned_df['Booster Landing'].apply(
        lambda x: x.split('(')[0].strip() if pd.notna(x) else x)

    # Drop original columns
    columns_to_drop = [
        'Date and\ntime (UTC)', 'Version,\nbooster', 'Launch\nsite']
    cleaned_df = cleaned_df.drop(columns=columns_to_drop)

    # Rename columns to be more concise and Python-friendly
    column_rename_map = {
        'Flight No.': 'flight_number',
        'Date': 'date',
        'Time (UTC)': 'time_utc',
        'Version': 'rocket_version',
        'Booster ID': 'booster_id',
        'Launch Site': 'launch_site',
        'Pad': 'launch_pad',
        'Payload': 'payload',
        'Payload mass': 'payload_mass',
        'Orbit': 'orbit',
        'Customer': 'customer',
        'Launch Outcome': 'launch_outcome',
        'Booster Landing': 'landing_outcome',
        'Landing Location': 'landing_site',
        'Description': 'description'
    }

    cleaned_df = cleaned_df.rename(columns=column_rename_map)

    # Convert date and time to Unix timestamp
    cleaned_df['timestamp'] = pd.to_datetime(
        cleaned_df['date'] + ' ' + cleaned_df['time_utc'], format='%d %B %Y %H:%M')

    # Convert to Pacific Time
    utc_tz = pytz.timezone('UTC')
    pacific_tz = pytz.timezone('America/Los_Angeles')

    def convert_to_pacific(ts):
        if pd.isna(ts):
            return None
        return utc_tz.localize(ts).astimezone(pacific_tz).strftime('%Y-%m-%d %H:%M:%S %Z')

    # Convert UTC to Pacific time
    cleaned_df['time_pacific'] = cleaned_df['timestamp'].apply(
        convert_to_pacific)

    # Split time_pacific into date and time
    cleaned_df[['new_date', 'time']] = cleaned_df['time_pacific'].str.split(
        ' ', n=1, expand=True)

    # Clean up time column to remove timezone
    cleaned_df['time'] = cleaned_df['time'].str.extract(r'(\d+:\d+:\d+)')

    # Drop unnecessary time columns
    columns_to_drop = ['time_utc', 'timestamp', 'time_pacific', 'date']
    existing_columns = [
        col for col in columns_to_drop if col in cleaned_df.columns]
    cleaned_df = cleaned_df.drop(columns=existing_columns)

    # Rename new_date to date
    cleaned_df = cleaned_df.rename(columns={'new_date': 'date'})

    return cleaned_df


# Apply the cleaning function to both dataframes
df2023_cleaned = clean_spacex_data(df2023)
df2024_cleaned = clean_spacex_data(df2024)
# %%
# Merge the cleaned dataframes
df = pd.concat([df2023_cleaned, df2024_cleaned], ignore_index=True)
df = df[df['launch_site'] == "Vandenberg"]
df['boostback'] = df['landing_site'].str.contains(
    'LZ', na=False) & df['landing_site'].str.contains('4', na=False)

# Convert date to datetime for comparison
df['date'] = pd.to_datetime(df['date'])

# Filter for date range
df = df[(df['date'] >= '2023-11-16') & (df['date'] <= '2024-02-05')]

# Reset index after filtering
df = df.reset_index(drop=True)
# %%
df.to_csv('vandenberg_boostback.csv', index=False)
# %%
