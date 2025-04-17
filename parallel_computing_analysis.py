import dask.dataframe as dd
import time

# Load the cleaned dataset
df_full = dd.read_csv('Cleaned_Trips_Full_Data.csv')

# Function to compute total trips and measure computation time
def compute_total_trips(df, label):
    start_time = time.time()
    total_trips = df['Trips'].sum().compute()
    end_time = time.time()
    duration = end_time - start_time
    print(f"{label} → Total Trips: {total_trips:.2f} computed in {duration:.4f} seconds\n")
    return total_trips, duration

# 🔸 Serial-style computation (Dask default, no repartitioning)
print("🔸 Serial-style processing (Default Scheduler)")
serial_total, serial_time = compute_total_trips(df_full, "Serial Processing")

# 🔹 Parallel computation with 4 partitions
df_part4 = df_full.repartition(npartitions=4)
print("🔹 Parallel Processing with 4 Partitions")
part4_total, part4_time = compute_total_trips(df_part4, "4 Partitions")

# 🔹 Parallel computation with 8 partitions
df_part8 = df_full.repartition(npartitions=8)
print("🔹 Parallel Processing with 8 Partitions")
part8_total, part8_time = compute_total_trips(df_part8, "8 Partitions")

# 🔹 Parallel computation with 16 partitions
df_part16 = df_full.repartition(npartitions=16)
print("🔹 Parallel Processing with 16 Partitions")
part16_total, part16_time = compute_total_trips(df_part16, "16 Partitions")
