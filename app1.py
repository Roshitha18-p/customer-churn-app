import streamlit as st
import pandas as pd
import pickle

# load trained files
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
features = pickle.load(open("features.pkl", "rb"))

# page config
st.set_page_config(
    page_title="Customer Churn Prediction",
    layout="centered"
)

# title
st.markdown("<h1 style='text-align: center;'>📊 Customer Churn Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Check whether a customer is likely to churn</p>", unsafe_allow_html=True)

st.markdown("---")

# input section
st.subheader("🔹 Enter Customer Details")

tenure = st.slider("Tenure (in months)", 0, 72, 12)
monthly = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
total = st.number_input("Total Charges", 0.0, 10000.0, 800.0)

# prepare input
input_df = pd.DataFrame({
    "tenure": [tenure],
    "MonthlyCharges": [monthly],
    "TotalCharges": [total]
})

# add missing columns
for col in features:
    if col not in input_df.columns:
        input_df[col] = 0

input_df = input_df[features]
scaled_input = scaler.transform(input_df)

st.markdown("---")

# prediction
if st.button("🔍 Predict Churn"):
    prob = model.predict_proba(scaled_input)[0][1]

    st.subheader("📌 Prediction Result")

    if prob >= 0.5:
        st.error(f"⚠️ **Customer is likely to churn**\n\nChurn Probability: **{prob:.2f}**")
    else:
        st.success(f"✅ **Customer is not likely to churn**\n\nChurn Probability: **{prob:.2f}**")

    # simple explanation
    st.info(
        "ℹ️ **How to read this:**\n"
        "- Probability closer to **1** → higher chance of churn\n"
        "- Probability closer to **0** → lower chance of churn"
    )

st.markdown("---")
st.caption("Built with Python, Scikit-learn & Streamlit")
