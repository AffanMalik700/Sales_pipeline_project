📊 End-to-End Sales Data Pipeline with Machine Learning
🚀 Overview
This project builds a complete data pipeline that:

Ingests raw CSV sales data

Cleans and stores it in a PostgreSQL database

Segregates data by business use cases (regions)

Applies a machine learning model to predict revenue

Stores predictions back into the database

🧠 Architecture
Plaintext
CSV → Pandas → PostgreSQL → Feature Engineering → ML Model → Predictions → PostgreSQL
⚙️ Tech Stack
Python (Pandas, NumPy)

PostgreSQL

SQLAlchemy

Scikit-learn

dotenv (for secure DB connection)

📂 Repository File Structure
Plaintext
Sales_pipeline_project/
│
├── Sales_pipeline_Script.py   # Main Python script for ETL and ML pipeline
├── ActualData.csv             # Raw dataset (Excluded via .gitignore)
├── .env                       # Environment variables (DB credentials - DO NOT COMMIT)
├── .gitignore                 # Specifies intentionally untracked files
├── requirements.txt           # List of Python dependencies
└── README.md                  # Project documentation
📥 Data Ingestion
Reads raw dataset (ActualData.csv) using Pandas

Loads full dataset into PostgreSQL table: sales

Python
df = pd.read_csv('ActualData.csv')
df.to_sql('sales', engine, if_exists='replace', index=False)
🧩 Data Segregation
Splits dataset by region

Creates separate tables for each region

Python
regions = df['region'].unique()
👉 Enables region-specific analysis and use cases.

🧪 Feature Engineering
Created interaction feature:

price_x_units = units_sold * unit_price

Encoded categorical variable:

month → one-hot encoding

🤖 Machine Learning Model
Model Used:
Linear Regression

Inputs:
Units sold

Unit price

Discount percentage

Month (encoded)

Engineered feature (price_x_units)

📊 Model Evaluation
R² Score: 0.9888 (measures how well the model explains variance)

RMSE: 1348.89 (measures prediction error magnitude)

🔮 Predictions Storage
Predictions are stored in a new PostgreSQL table: predictions

Python
results_df.to_sql('predictions', engine, if_exists='replace', index=False)
🗄️ Database Tables
sales → full master dataset

region_* → segmented tables for specific territories

predictions → ML output alongside actuals

🔐 Environment Setup
Uses a .env file to securely store database credentials so they are never exposed in the source code:

Code snippet
DB_URL="postgresql://username:password@localhost:5432/your_database_name"
▶️ How to Run
1. Clone the repository

Bash
git clone https://github.com/AffanMalik700/Sales_pipeline_project.git
cd Sales_pipeline_project
2. Set up a virtual environment (Recommended)

Bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
3. Install dependencies

Bash
pip install -r requirements.txt
4. Run the pipeline

Bash
python Sales_pipeline_Script.py
🎯 Key Learnings
Built an end-to-end ETL pipeline

Integrated SQL with Pandas

Designed a data segregation strategy

Applied feature engineering techniques

Deployed ML predictions into a database

🚧 Future Improvements
[ ] Automate pipeline (Airflow / cron)

[ ] Add data validation layer (Pydantic / Great Expectations)

[ ] Improve model (Upgrade to tree-based models like XGBoost or Random Forest)

[ ] Connect to cloud storage (Pull raw data directly from AWS S3)

📌 Conclusion
This project demonstrates how raw data can be transformed into structured, queryable, and predictive insights using a combination of data engineering and machine learning techniques.