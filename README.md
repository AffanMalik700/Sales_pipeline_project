# 📊 End-to-End Sales Data Pipeline with Machine Learning

## 🚀 Overview

This project builds a complete data pipeline that:

* Ingests raw CSV sales data
* Cleans and stores it in a PostgreSQL database
* Segregates data by business use cases (regions)
* Applies a machine learning model to predict revenue
* Stores predictions back into the database

---

## 🧠 Architecture

```text
CSV → Pandas → PostgreSQL → Feature Engineering → ML Model → Predictions → PostgreSQL
```

---

## ⚙️ Tech Stack

* Python (Pandas, NumPy)
* PostgreSQL
* SQLAlchemy
* Scikit-learn
* dotenv (for secure DB connection)

---

## 📥 Data Ingestion

* Reads raw dataset (`ActualData.csv`) using Pandas
* Loads full dataset into PostgreSQL table: `sales`

```python
df = pd.read_csv('ActualData.csv')
df.to_sql('sales', engine, if_exists='replace', index=False)
```

---

## 🧩 Data Segregation

* Splits dataset by `region`
* Creates separate tables for each region

```python
regions = df['region'].unique()
```

👉 Enables region-specific analysis and use cases

---

## 🧪 Feature Engineering

* Created interaction feature:

  * `price_x_units = units_sold * unit_price`
* Encoded categorical variable:

  * `month` → one-hot encoding

---

## 🤖 Machine Learning Model

### Model Used:

* Linear Regression

### Inputs:

* Units sold
* Unit price
* Discount percentage
* Month (encoded)
* Engineered feature

---

## 📊 Model Evaluation

* R² Score (model accuracy)
* RMSE (error metric)

```text
R² Score: measures how well model explains variance  
RMSE: measures prediction error magnitude  
```

---

## 🔮 Predictions Storage

* Predictions are stored in PostgreSQL table: `predictions`

```python
results_df.to_sql('predictions', engine, if_exists='replace', index=False)
```

---

## 🗄️ Database Tables

* `sales` → full dataset
* `region_*` → segmented tables
* `predictions` → ML output

---

## 🔐 Environment Setup

Uses `.env` file to securely store database credentials:

```env
DB_URL=postgresql+psycopg://user@localhost:5432/sales_db
```

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python main.py
```

---

## 🎯 Key Learnings

* Built an end-to-end ETL pipeline
* Integrated SQL with Pandas
* Designed data segregation strategy
* Applied feature engineering techniques
* Deployed ML predictions into database

---

## 🚧 Future Improvements

* Automate pipeline (Airflow / cron)
* Add data validation layer
* Improve model (tree-based models)
* Connect to cloud storage (AWS S3)

---

## 📌 Conclusion

This project demonstrates how raw data can be transformed into structured, queryable, and predictive insights using a combination of data engineering and machine learning techniques.
