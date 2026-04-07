# Customer Churn Prediction Dashboard

🚀 This project includes a Streamlit dashboard for predicting customer churn using machine learning.

## Overview
This project analyzes customer behavior and predicts whether a customer is likely to churn.

It combines:
- Data cleaning and preprocessing
- Exploratory data analysis (EDA)
- Machine learning modeling
- Model improvement
- Interactive Streamlit dashboard

---

## Key Insights
- Month-to-month contract customers have the highest churn
- Customers with shorter tenure are more likely to leave
- Higher monthly charges are associated with higher churn

---

## Model
- Logistic Regression
- Improved using scaling and class balancing
- Focus on recall to detect more churn customers

---

## How to Run the App

### 1. Install dependencies
```bash
pip install -r requirements.txt

streamlit run app.py
