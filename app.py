import streamlit as st
import pandas as pd
import joblib

# load model, scaler, and columns
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
model_columns = joblib.load("columns.pkl")

# page config
st.set_page_config(page_title="Churn Dashboard", layout="centered")

# title
st.title("Customer Churn Prediction Dashboard")
st.write("Predict customer churn and support retention decisions using machine learning.")

# -----------------------
# USER INPUTS
# -----------------------

tenure = st.slider("Tenure (months)", 0, 72, 12)
monthly_charges = st.number_input("Monthly Charges", 0.0, 200.0, 50.0)
total_charges = st.number_input("Total Charges", 0.0, 10000.0, 1000.0)
senior = st.selectbox("Senior Citizen", [0, 1])

# -----------------------
# CREATE INPUT DATA
# -----------------------

input_data = pd.DataFrame({
    "SeniorCitizen": [senior],
    "tenure": [tenure],
    "MonthlyCharges": [monthly_charges],
    "TotalCharges": [total_charges]
})

# encode like training
input_data = pd.get_dummies(input_data)

# align columns
input_data = input_data.reindex(columns=model_columns, fill_value=0)

# scale
input_scaled = scaler.transform(input_data)

# -----------------------
# PREDICTION
# -----------------------

if st.button("Predict Churn"):

    prediction = model.predict(input_scaled)[0]
    prob = model.predict_proba(input_scaled)[0][1]

    st.subheader("Prediction Result")

    # business logic display
    if prob > 0.7:
        st.error(f"High Risk of Churn ❌ ({prob:.2f})")
        st.write("👉 Action: Offer retention incentives or customer support.")
    elif prob > 0.4:
        st.warning(f"Moderate Risk ⚠️ ({prob:.2f})")
        st.write("👉 Action: Monitor and engage with the customer.")
    else:
        st.success(f"Low Risk ✅ ({prob:.2f})")
        st.write("👉 Action: Customer likely to stay.")

    # optional debug info (good for demo)
    with st.expander("See Input Data"):
        st.write(input_data)
