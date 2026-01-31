# Customer Churn Prediction App

## Overview
This project is a **Customer Churn Prediction app** built using **Python, Scikit-learn, and Streamlit**.  
The app predicts whether a customer is likely to **leave (churn)** a subscription-based service, such as a telecom company. It also shows the **probability of churn** based on the customer’s details.

The project demonstrates the full **data science workflow**:
- Data cleaning
- Exploratory Data Analysis (EDA)
- Feature engineering
- Model building and evaluation
- Deployment using Streamlit

---

## Dataset
We used the **Telco Customer Churn Dataset** (available on Kaggle / IBM).  
It includes customer information such as:
- Tenure
- Monthly charges
- Total charges
- Contract type
- Other demographic and service features

---

## How It Works

1. **Data Cleaning & Preprocessing**
   - Handle missing values
   - Convert categorical features into numeric (one-hot encoding)
   - Scale numeric features

2. **Model**
   - Logistic Regression is used to predict churn
   - Trained using 80% of the data (train set)
   - Tested on 20% of the data (test set)
   - Model performance is evaluated using accuracy and classification report

3. **Streamlit App**
   - User enters customer details:
     - Tenure
     - Monthly charges
     - Total charges
   - App outputs:
     - **Churn prediction** (Yes / No)
     - **Churn probability** (0–1)

---

## Folder Structure
customer-churn-app/
│
├── app.py # Streamlit app
├── model.pkl # Trained model
├── scaler.pkl # Scaler for numeric features
├── features.pkl # Feature column names
├── requirements.txt # Required Python libraries
└── README.md # This file

## How to Run

### Option 1: Streamlit Cloud (Recommended)
1. Go to [Streamlit Cloud](https://streamlit.io/cloud)
2. Sign in with GitHub
3. Deploy the repository with `app.py` as the main file
4. Open the provided URL and use the app (https://roshitha18-p-customer-churn-app-app1-jjq2ru.streamlit.app)
