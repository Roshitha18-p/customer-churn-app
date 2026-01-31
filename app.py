import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
features = pickle.load(open("features.pkl", "rb"))

st.title("Customer Churn Prediction")

tenure = st.number_input("Tenure (months)", 0, 72)
monthly = st.number_input("Monthly Charges", 0.0, 200.0)
total = st.number_input("Total Charges", 0.0, 10000.0)

input_df = pd.DataFrame({
    "tenure": [tenure],
    "MonthlyCharges": [monthly],
    "TotalCharges": [total]
})

for col in features:
    if col not in input_df.columns:
        input_df[col] = 0

input_df = input_df[features]
scaled = scaler.transform(input_df)

if st.button("Predict"):
    pred = model.predict(scaled)[0]
    prob = model.predict_proba(scaled)[0][1]
    st.write("Churn probability:", round(prob, 2))
