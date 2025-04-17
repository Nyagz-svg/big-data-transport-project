
import dask.dataframe as dd

# Define column data types
dtypes_dict = {
    'County Name': 'object',
    'State Postal Code': 'object',
    'Number of Trips': 'float64',
    'Number of Trips 1-3': 'float64',
    'Number of Trips 3-5': 'float64',
    'Number of Trips 5-10': 'float64',
    'Number of Trips 10-25': 'float64',
    'Number of Trips 25-50': 'float64',
    'Number of Trips 50-100': 'float64',
    'Number of Trips 100-250': 'float64',
    'Number of Trips 250-500': 'float64',
    'Number of Trips >=500': 'float64',
    'Number of Trips <1': 'float64',
    'Population Not Staying at Home': 'float64',
    'Population Staying at Home': 'float64'
}

# Load dataset
df_dist = dd.read_csv('Cleaned_Trips_By_Distance.csv', dtype=dtypes_dict)

# Categorise trips by distance
def categorize_trips(df):
    df['Short Distance Trips'] = (
        df['Number of Trips <1'] +
        df['Number of Trips 1-3'] +
        df['Number of Trips 3-5'] +
        df['Number of Trips 5-10']
    )
    df['Medium Distance Trips'] = (
        df['Number of Trips 10-25'] +
        df['Number of Trips 25-50'] +
        df['Number of Trips 50-100']
    )
    df['Long Distance Trips'] = (
        df['Number of Trips 100-250'] +
        df['Number of Trips 250-500'] +
        df['Number of Trips >=500']
    )
    return df

# Apply function
df_dist = df_dist.map_partitions(categorize_trips)

# Save updated dataset
df_dist.compute().to_csv('Categorised_Trips_By_Distance.csv', index=False)
print("✅ Categorisation complete.")
