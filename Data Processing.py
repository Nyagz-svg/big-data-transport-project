import dask.dataframe as dd
import pandas as pd
import time

# Load the cleaned CSVs
df_dask = dd.read_csv('Cleaned_Trips_Full_Data.csv')
df_pandas = pd.read_csv('Cleaned_Trips_Full_Data.csv')

# Serial processing using Pandas
start_time = time.time()
total_pandas = df_pandas['Trips'].sum()
end_time = time.time()
print(f"Serial (Pandas) ➤ Total Trips: {total_pandas:.2f} computed in {end_time - start_time:.4f} seconds")

# Parallel processing using Dask
start_time = time.time()
total_dask = df_dask['Trips'].sum().compute()
end_time = time.time()
print(f"Parallel (Dask) ➤ Total Trips: {total_dask:.2f} computed in {end_time - start_time:.4f} seconds")
