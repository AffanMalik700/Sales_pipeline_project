# ==========================================
# 1. Imports and Setup
# ==========================================
import os
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from dotenv import load_dotenv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# ==========================================
# 2. Database Connection
# ==========================================
# Load environment variables (like passwords) securely
load_dotenv()
# Create a connection engine to PostgreSQL using the URL from the .env file
engine = create_engine(os.getenv('DB_URL'))

# ==========================================
# 3. Data Ingestion & Storage
# ==========================================
# Load the raw data from a CSV file into a Pandas DataFrame
df = pd.read_csv('ActualData.csv')

# Save the entire raw dataset directly into the SQL database as a table named 'sales'
df.to_sql('sales', engine, if_exists='replace', index=False)

# Split the data by region and create a separate SQL table for each region
regions = df['region'].unique()
for region in regions:
    region_df = df[df['region'] == region]
    region_df.to_sql(region, engine, if_exists='replace', index=False)

# ==========================================
# 4. Feature Engineering for Machine Learning
# ==========================================
# Select the features (X) and the target variable to predict (y)
# Note: .copy() is used to prevent the SettingWithCopyWarning
X = df[['units_sold', 'unit_price', 'discount_pct', 'month']].copy()
y = df['revenue']

# Create a new engineered feature: total base price before discounts
X['price_x_units'] = X['units_sold'] * X['unit_price']

# Convert the categorical 'month' column into numerical dummy variables (One-Hot Encoding)
X = pd.get_dummies(X, columns=['month'])

# ==========================================
# 5. Model Training & Evaluation
# ==========================================
# Split the dataset into training data (80%) and testing data (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Generate predictions on the test dataset
y_pred = model.predict(X_test)

# Calculate model performance metrics
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"R² Score: {r2:.4f}")
print(f"RMSE: {rmse:.2f}")

# ==========================================
# 6. Saving Predictions
# ==========================================
# Create a new DataFrame to store the test data alongside actual and predicted revenues
results_df = X_test.copy()
results_df['actual_revenue'] = y_test.values
results_df['predicted_revenue'] = y_pred

# Save the final prediction results back into the database
results_df.to_sql('predictions', engine, if_exists='replace', index=False)
print("Predictions stored successfully")