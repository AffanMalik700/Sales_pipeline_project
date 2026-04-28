# 📊 Sales Data Pipeline with Machine Learning

An end-to-end data engineering and machine learning system that ingests raw sales data, transforms it into a structured relational database, and generates revenue predictions using a regression model.

---

## 🚀 Overview

This project demonstrates how raw, unstructured data can be converted into a reliable, queryable, and predictive system.

It solves key real-world challenges:

* messy CSV data (missing values, inconsistent formats)
* lack of structure for analysis
* need for predictive insights from historical data

---

## 🧠 Key Features

### 🔹 End-to-End Data Pipeline (ETL)

* Extracts raw data from CSV
* Cleans and standardizes data using Pandas
* Loads structured data into PostgreSQL

---

### 🔹 Data Segregation & Modeling

* Splits dataset into:

  * `customers` (master data)
  * `sales` (transaction data)
* Establishes relationships using `customer_id` (primary/foreign key)

---

### 🔹 Database Integration

* Uses SQLAlchemy to connect Python with PostgreSQL
* Stores:

  * raw structured data (`sales`, `customers`)
  * predictions (`predictions` table)

---

### 🔹 Feature Engineering

* Created interaction feature:

  * `price_x_units = units_sold × unit_price`
* Applied encoding:

  * one-hot encoding for categorical variables (`month`)

---

### 🔹 Machine Learning Model

* Model: Linear Regression
* Predicts: `revenue`

---

## ⚙️ Tech Stack

* **Backend:** Python
* **Data Processing:** Pandas, NumPy
* **Database:** PostgreSQL
* **ORM/Connector:** SQLAlchemy
* **ML:** Scikit-learn
* **Environment Management:** dotenv

---

## 🔄 Data Pipeline

```text id="bvrg5q"
CSV → Pandas Cleaning → Data Segregation → PostgreSQL → Feature Engineering → ML Model → Predictions → PostgreSQL
```

---

## 🗄️ Database Design

### Customers Table

```text id="7cuyg6"
customer_id | customer | city
```

### Sales Table

```text id="2f9cxb"
order_id | customer_id | amount | date
```

### Predictions Table

```text id="gfg4qh"
features | actual_revenue | predicted_revenue
```

---

## 📊 Model Performance

* **R² Score:** 0.9888
* **RMSE:** 1348.89

> High performance achieved through feature engineering, particularly the interaction feature between units sold and unit price.

---

## 🔐 Environment Setup

Database connection is managed securely using `.env`:

```env id="0lcvgu"
DB_URL=postgresql+psycopg:///sales_db
```

---

## ▶️ How to Run

```bash id="l8sajx"
git clone <your-repo-link>
cd your-project

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python main.py
```

---

## 💡 Key Learnings

* Designing and implementing ETL pipelines
* Transforming raw data into relational database structures
* Integrating SQL with Python workflows
* Importance of feature engineering in ML performance
* Storing and reusing predictions in databases

---

## 🚧 Future Improvements

* Automate pipeline execution (Airflow / cron jobs)
* Integrate cloud storage (AWS S3)
* Improve model with advanced algorithms (XGBoost, Random Forest)
* Add data validation and monitoring

---

## 📌 Conclusion

This project demonstrates how to move beyond simple data analysis by building a complete system that:

* processes raw data
* structures it for efficient querying
* generates predictive insights

It reflects a transition from working with files to building scalable data systems.
