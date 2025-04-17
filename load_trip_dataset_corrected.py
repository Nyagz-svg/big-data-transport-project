
import dask.dataframe as dd

# Load dataset with appropriate dtype mapping based on actual data
df_dist = dd.read_csv('Trip by dataset.csv', dtype={
    'State Postal Code': 'object',
    'County Name': 'object',
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
})

# Preview rows to confirm successful load
print(df_dist.head())
