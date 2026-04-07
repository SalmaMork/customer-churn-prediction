# Customer Churn Prediction Dashboard

🚀 This project presents a machine learning-powered Streamlit dashboard to predict customer churn and support business retention strategies.

---

## 📌 Overview

This project analyzes telecom customer behavior and predicts whether a customer is likely to churn.

It combines:
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Machine learning modeling (Logistic Regression)
- Model improvement using scaling and class balancing
- An interactive Streamlit dashboard

The goal is to help businesses identify at-risk customers and take proactive actions.

---

## 💼 Business Problem

Customer churn leads to revenue loss and increased acquisition costs.

This project helps answer:
- Which customers are most likely to churn?
- What factors influence churn?
- How can we detect at-risk customers early?

---

## 📊 Key Insights

- Customers on **month-to-month contracts** have the highest churn rate  
- Customers with **short tenure** are more likely to leave  
- Higher **monthly charges** are associated with higher churn  

👉 These insights can guide retention strategies such as pricing adjustments and customer engagement.

---

## 🤖 Machine Learning Model

- Model: Logistic Regression  
- Features: Customer demographics and billing data  

### Initial Model
- Accuracy: ~79%  
- Churn Recall: ~52%  

### Improved Model
- Accuracy: ~73%  
- Churn Recall: ~79%  

👉 The improved model prioritizes **recall**, ensuring more at-risk customers are identified, which is more valuable from a business perspective.

---

## 🌐 Streamlit Dashboard

The app allows users to:
- Input customer information  
- Predict churn probability  
- View risk level (Low / Moderate / High)  
- Receive suggested business actions  

---
## ⚙️ How to Run the App

Follow these steps to run the project locally:

### 1. Clone the repository
```bash
git clone https://github.com/SalmaMork/customer-churn-prediction.git
cd customer-churn-prediction
```
### 2. Install dependencies
```bash 
pip install -r requirements.txt
```
### 3. Run the Streamlit app
```bash
streamlit run app.py
```
### 4. Open in browser
```bash
http://localhost:8501
```
## 🛠️ Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib / Seaborn
- Streamlit
- Joblib

---
👩‍💻 Author
- Salma Morkani
