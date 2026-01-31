# Customer Churn Prediction - Student-Style Streamlit App

import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt

# 1. Load trained model, scaler, features
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
features = pickle.load(open("features.pkl", "rb"))

# Feature importance for top reasons behind churn
import numpy as np
coefficients = pd.Series(model.coef_[0], index=features)
coefficients = coefficients.sort_values(ascending=False)

# 2. Streamlit page setup
st.set_page_config(page_title="Customer Churn Prediction", layout="centered")
st.markdown("<h1 style='text-align: center;'>📊 Customer Churn Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>A simple student project to predict if a customer might leave</p>", unsafe_allow_html=True)
st.markdown("---")

# 3. User inputs
st.subheader("🔹 Enter Customer Details")
tenure = st.slider("Tenure (months)", 0, 72, 12)
monthly = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
total = st.number_input("Total Charges", 0.0, 10000.0, 800.0)

input_df = pd.DataFrame({"tenure":[tenure], "MonthlyCharges":[monthly], "TotalCharges":[total]})
for col in features:
    if col not in input_df.columns:
        input_df[col] = 0
input_df = input_df[features]
scaled_input = scaler.transform(input_df)

st.markdown("---")

# 4. Prediction
if st.button("🔍 Predict Churn"):
    prob = model.predict_proba(scaled_input)[0][1]
    st.subheader("📌 Prediction Result")
    if prob >= 0.5:
        st.error(f"⚠️ Customer is likely to churn\nChurn Probability: **{prob:.2f}**")
    else:
        st.success(f"✅ Customer is not likely to churn\nChurn Probability: **{prob:.2f}**")
    st.info("ℹ️ Probability closer to 1 → customer might leave. Closer to 0 → customer likely stays.")

    # 5. Top reasons behind churn
    st.subheader("🔹 Top Factors Affecting Churn")
    st.write("Red bars → increase chance of churn, Green bars → reduce chance of churn")

    # Red bars - increase churn
    fig, ax = plt.subplots(figsize=(8,4))
    coefficients.head(10).plot(kind='bar', color='red', ax=ax)
    plt.ylabel("Coefficient Value")
    st.pyplot(fig)

    # Green bars - reduce churn
    fig2, ax2 = plt.subplots(figsize=(8,4))
    coefficients.tail(10).plot(kind='bar', color='green', ax=ax2)
    plt.ylabel("Coefficient Value")
    st.pyplot(fig2)


