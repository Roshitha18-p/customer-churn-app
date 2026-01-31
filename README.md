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
ill

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
 Streamlit Cloud
1. Go to [Streamlit Cloud](https://streamlit.io/cloud)
2. Sign in with GitHub
3. Deploy the repository with `app.py` as the main file
4. Open the provided URL and use the app (https://roshitha18-p-customer-churn-app-app1-jjq2ru.streamlit.app)

## Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Matplotlib, Seaborn

## Key Learnings
- Full **ML pipeline** from raw data to deployed app
- Handling **categorical & numeric data**
- Building and evaluating a **classification model**
- Deploying a **real-time web app** using Streamlit

## Future Improvements
- Add more **interactive charts** in the app
- Include **feature importance** explanations for each prediction
- Experiment with other models (Decision Tree, Random Forest)
- Add **user authentication** for enterprise use
