
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Customer Churn Prediction",
    layout="centered"
)

@st.cache_resource
def load_artifacts():
    return (
        joblib.load("model.pkl"),
        joblib.load("scaler.pkl"),
        joblib.load("columns.pkl"),
    )

model, scaler, model_columns = load_artifacts()

st.title("📊 Customer Churn Prediction")
st.write(
    "Estimate customer churn risk using a trained "
    "logistic regression model."
)

st.subheader("Customer information")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Female", "Male"])
    senior = st.selectbox("Senior citizen", [0, 1])
    partner = st.selectbox("Has partner?", ["No", "Yes"])
    dependents = st.selectbox("Has dependents?", ["No", "Yes"])
    tenure = st.slider("Tenure (months)", 0, 72, 12)
    phone = st.selectbox("Phone service", ["No", "Yes"])

    if phone == "No":
        multiple_lines = "No phone service"
        st.info("Multiple lines: No phone service")
    else:
        multiple_lines = st.selectbox(
            "Multiple lines",
            ["No", "Yes"]
        )

    internet = st.selectbox(
        "Internet service",
        ["DSL", "Fiber optic", "No"]
    )

    if internet == "No":
        online_security = "No internet service"
        online_backup = "No internet service"
        st.info("Online security and backup: No internet service")
    else:
        online_security = st.selectbox(
            "Online security",
            ["No", "Yes"]
        )
        online_backup = st.selectbox(
            "Online backup",
            ["No", "Yes"]
        )

with col2:
    if internet == "No":
        device_protection = "No internet service"
        tech_support = "No internet service"
        streaming_tv = "No internet service"
        streaming_movies = "No internet service"
        st.info("Other internet-dependent services: No internet service")
    else:
        device_protection = st.selectbox(
            "Device protection", ["No", "Yes"]
        )
        tech_support = st.selectbox(
            "Tech support", ["No", "Yes"]
        )
        streaming_tv = st.selectbox(
            "Streaming TV", ["No", "Yes"]
        )
        streaming_movies = st.selectbox(
            "Streaming movies", ["No", "Yes"]
        )
    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )
    paperless = st.selectbox(
        "Paperless billing",
        ["No", "Yes"]
    )
    payment = st.selectbox(
        "Payment method",
        [
            "Bank transfer (automatic)",
            "Credit card (automatic)",
            "Electronic check",
            "Mailed check"
        ]
    )
    monthly_charges = st.number_input(
        "Monthly charges", min_value=0.0, value=50.0
    )
    total_charges = st.number_input(
        "Total charges", min_value=0.0, value=1000.0
    )

if st.button("Predict Churn", type="primary"):

    raw_input = pd.DataFrame([{
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone,
        "MultipleLines": multiple_lines,
        "InternetService": internet,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless,
        "PaymentMethod": payment,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }])

    # Recover the categorical levels used in training.
    training_data = pd.read_csv("data.csv")

    categorical_columns = raw_input.select_dtypes(
        include=["object"]
    ).columns

    for column in categorical_columns:
        categories = sorted(
            training_data[column].dropna().unique()
        )
        raw_input[column] = pd.Categorical(
            raw_input[column],
            categories=categories
        )

    # Match training encoding: get_dummies(drop_first=True).
    encoded_input = pd.get_dummies(
        raw_input, drop_first=True
    )

    encoded_input = encoded_input.reindex(
        columns=model_columns, fill_value=0
    ).astype(float)

    scaled_input = scaler.transform(encoded_input)

    churn_index = list(model.classes_).index(1)
    probability = model.predict_proba(scaled_input)[0][
        churn_index
    ]

    st.subheader("Prediction result")
    st.metric("Estimated churn probability", f"{probability:.1%}")

    if probability >= 0.7:
        st.error("High churn risk")
        st.write("Consider proactive customer outreach.")
    elif probability >= 0.4:
        st.warning("Moderate churn risk")
        st.write("Consider monitoring customer satisfaction.")
    else:
        st.success("Low churn risk")
        st.write("No immediate retention intervention suggested.")

    st.caption(
        "Risk bands are illustrative and have not yet "
        "been validated as business decision thresholds."
    )

    with st.expander("View customer inputs"):
        st.dataframe(raw_input)
