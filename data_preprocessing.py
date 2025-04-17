
import dask.dataframe as dd

# Load both datasets
df_full = dd.read_csv('Trips full data.csv')
df_dist = dd.read_csv('Trip by dataset.csv', dtype={
    'State Postal Code': 'object',
    'County Name': 'object',
    'Number of Trips >=500': 'float64'
})

# Drop duplicate rows if any
df_full = df_full.drop_duplicates()
df_dist = df_dist.drop_duplicates()

# Check and print missing values
print("\nMissing values in Trips_Full_Data:")
print(df_full.isnull().sum().compute())

print("\nMissing values in Trips_By_Distance:")
print(df_dist.isnull().sum().compute())

# Fill missing numerical values with column mean
df_full = df_full.map_partitions(lambda df: df.fillna(df.mean(numeric_only=True)))
df_dist = df_dist.map_partitions(lambda df: df.fillna(df.mean(numeric_only=True)))

# Confirm post-cleaning status
print("\nPost-cleaning check - Missing values in Trips_Full_Data:")
print(df_full.isnull().sum().compute())

print("\nPost-cleaning check - Missing values in Trips_By_Distance:")
print(df_dist.isnull().sum().compute())
