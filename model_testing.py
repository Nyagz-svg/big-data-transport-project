# 2.8 Model Testing – Train/Test Split and Evaluation

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load cleaned dataset
df = pd.read_csv('Cleaned_Trips_Full_Data.csv')

# Define features and target variable
X = df[['People Not Staying at Home']]  # correct column name
y = df['Trips']

# Split into training and test sets (80/20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Fit linear regression model on training data
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Evaluate model performance
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"✅ Test MSE: {mse:.2f}")
print(f"✅ Test R²: {r2:.4f}")

# Visualise actual vs predicted
plt.figure(figsize=(8, 6))
plt.scatter(X_test, y_test, color='blue', alpha=0.6, label='Actual')
plt.scatter(X_test, y_pred, color='red', alpha=0.6, label='Predicted')
plt.title('Model Testing – Actual vs Predicted Trips')
plt.xlabel('People Not Staying at Home')
plt.ylabel('Trips')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
