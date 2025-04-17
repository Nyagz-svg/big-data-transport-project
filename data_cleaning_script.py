
import pandas as pd
import dask.dataframe as dd

# Explicit column data types for Trip by dataset.csv
dtypes_dict = {
    'County Name': 'object',
    'State Postal Code': 'object',
    'Number of Trips': 'float64',
    'Number of Trips 1-3': 'float64',
    'Number of Trips 10-25': 'float64',
    'Number of Trips 100-250': 'float64',
    'Number of Trips 25-50': 'float64',
    'Number of Trips 250-500': 'float64',
    'Number of Trips 3-5': 'float64',
    'Number of Trips 5-10': 'float64',
    'Number of Trips 50-100': 'float64',
    'Number of Trips <1': 'float64',
    'Number of Trips >=500': 'float64',
    'Population Not Staying at Home': 'float64',
    'Population Staying at Home': 'float64'
}

# Load datasets with correct dtypes
df_dist = dd.read_csv('Trip by dataset.csv', dtype=dtypes_dict)
df_full = dd.read_csv('Trips full data.csv')

# Check for missing values
print("Missing values in Trips_Full_Data:")
print(df_full.isnull().sum().compute())

print("\nMissing values in Trips_By_Distance:")
print(df_dist.isnull().sum().compute())

# Drop duplicates
df_full = df_full.drop_duplicates()
df_dist = df_dist.drop_duplicates()

# Fill missing values using forward-fill (Dask-compatible)
df_full = df_full.ffill()
df_dist = df_dist.ffill()

# Save cleaned versions
df_full.compute().to_csv('Cleaned_Trips_Full_Data.csv', index=False)
df_dist.compute().to_csv('Cleaned_Trips_By_Distance.csv', index=False)

print("\n✅ Cleaning complete! Cleaned files saved.")
