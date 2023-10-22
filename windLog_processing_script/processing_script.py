import os
import sqlite3
import pandas as pd
from datetime import datetime

# Get the current date in YYYYMMDD format
current_date = datetime.now().strftime("%Y%m%d")

# Define the directory path where the s3db files are located
directory_path = '/Users/kylenessen/Library/CloudStorage/OneDrive-Althouse&Meade,Inc/Masters/WindLog'

# Initialize an empty DataFrame to hold all the data
final_df = pd.DataFrame()

# Step 1: List all s3db files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.s3db'):
        filepath = os.path.join(directory_path, filename)
        
        # Step 2: Read s3db file into DataFrame
        with sqlite3.connect(filepath) as conn:
            data = pd.read_sql_query("SELECT * FROM Wind", conn)
        
        # Step 3: Filter and Rename Columns
        data = data.drop(columns=['id'])
        sensor_name = filename.replace('.s3db', '')
        data['sensor_name'] = sensor_name
        
        # Step 4: Combine DataFrames
        final_df = pd.concat([final_df, data], ignore_index=True)

# Step 5: Handle Duplicates
final_df.drop_duplicates(inplace=True)

# Step 6: Export to CSV with Date Appended
final_csv_path = f'combined_wind_data_{current_date}.csv'
final_df.to_csv("pismo_wind_data/"+final_csv_path, index=False)

final_csv_path
