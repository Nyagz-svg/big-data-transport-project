import dask.dataframe as dd
import time

# Load the cleaned datasets (adjust paths if necessary)
df_full = dd.read_csv('Cleaned_Trips_Full_Data.csv')
df_dist = dd.read_csv('Cleaned_Trips_By_Distance.csv')

# Function to test parallel processing: computes sum of trips
def compute_total_trips(df, label):
    start_time = time.time()
    total_trips = df['Trips'].sum().compute()
    end_time = time.time()
    duration = end_time - start_time
    print(f"{label} Total Trips: {total_trips:.2f} computed in {duration:.4f} seconds\n")
    return total_trips, duration

# Run computation on df_full
print("🔁 Serial-style processing (Dask default scheduler):")
serial_result = compute_total_trips(df_full, "Full Dataset")

# You can repeat this with different number of Dask partitions for parallel testing
