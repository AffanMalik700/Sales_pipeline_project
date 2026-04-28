# 1. Imports
import pandas as pd
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
# 2. Connect
engine = create_engine('postgresql://affan@localhost:5432/sales_db')

# 3. Read CSV
df = pd.read_csv('ActualData.csv')

# 4. Write full table to PostgreSQL
df.to_sql('sales', engine, if_exists='replace', index=False)

# 5. Split by region and store
regions = df['region'].unique()
for region in regions:
    region_df = df[df['region'] == region]
    region_df.to_sql(region, engine, if_exists='replace', index=False)

# 6. Linear Regression
X = df[['units_sold', 'unit_price', 'discount_pct', 'month']]
y = df['revenue']
X['price_x_units'] = df['units_sold'] * df['unit_price']
X = pd.get_dummies(X, columns=['month'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# predicting
y_pred = model.predict(X_test)
#evaluating
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"R² Score: {r2:.4f}")
print(f"RMSE: {rmse:.2f}")

results_df = X_test.copy()
results_df['actual_revenue'] = y_test.values
results_df['predicted_revenue'] = y_pred

results_df.to_sql('predictions', engine, if_exists='replace', index=False)
print("Predictions stored successfully")

