import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df_full = pd.read_csv('Cleaned_Trips_Full_Data.csv')

# Convert 'Date' column to datetime for time series analysis
df_full['Date'] = pd.to_datetime(df_full['Date'], errors='coerce')

# 1. Trend Analysis: Trips over time
df_trend = df_full.groupby('Date')['Trips'].sum().reset_index()

plt.figure(figsize=(12, 5))
plt.plot(df_trend['Date'], df_trend['Trips'], marker='o', linestyle='-', alpha=0.8)
plt.title('Trips Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Total Trips')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Correlation Analysis: Identify strongest predictors
corr_cols = ['Trips', 'People Not Staying at Home', 'Population Staying at Home']
corr = df_full[corr_cols].corr()

plt.figure(figsize=(8, 5))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.tight_layout()
plt.show()

# Optional: Print correlation matrix
print("Correlation Matrix:\n", corr)
