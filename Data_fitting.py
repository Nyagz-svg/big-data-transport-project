import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load cleaned dataset
df_full = pd.read_csv('Cleaned_Trips_Full_Data.csv')

# Drop rows with missing or non-numeric data in relevant columns
df_full = df_full[['People Not Staying at Home', 'Trips']].dropna()
df_full = df_full.astype(float)

# Define independent (X) and dependent (y) variables
X = df_full[['People Not Staying at Home']]
y = df_full['Trips']

# Fit linear regression model
model = LinearRegression()
model.fit(X, y)

# Print model parameters
print(f"Intercept: {model.intercept_:.2f}")
print(f"Coefficient: {model.coef_[0]:.2f}")

# Predict and plot
y_pred = model.predict(X)

plt.scatter(X, y, color='lightblue', label='Actual')
plt.plot(X, y_pred, color='red', label='Fitted Line')
plt.xlabel('People Not Staying at Home')
plt.ylabel('Trips')
plt.title('Linear Regression Fit')
plt.legend()
plt.grid(True)
plt.show()
