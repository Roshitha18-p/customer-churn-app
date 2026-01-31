 Customer Churn Prediction App
 
## **Project Overview**
This is a **student project** to predict whether a customer is likely to leave (churn) a subscription-based service such as a telecom company.  

The project demonstrates an **end-to-end Data Science workflow**, including:  
- Data cleaning & preprocessing  
- Exploratory Data Analysis (EDA)  
- Feature engineering  
- Model building and evaluation  
- Deployment using **Streamlit** for interactive predictions  

---

## **Key Features**
- Predict **Churn** (Yes / No) based on customer details  
- Shows **Churn Probability** (0–1)  
- Displays **Top Factors** influencing customer churn (feature importance)  
- User-friendly **interactive Streamlit interface**  

---

## **Dataset**
- **Source:** [Telco Customer Churn Dataset](https://www.kaggle.com/blastchar/telco-customer-churn)  
- **Rows:** 7,043 | **Columns:** 21  
- **Key Features:**  
  - Tenure  
  - Monthly Charges  
  - Total Charges  
  - Contract Type  
  - Services & Demographics  
- **Target:** `Churn` (Yes = 1 / No = 0)  

## **Project Workflow**

### 1. Data Cleaning
- Converted `TotalCharges` to numeric  
- Filled missing values with median  
- Dropped `customerID` column  
- Encoded categorical variables using **one-hot encoding**  

### 2. Exploratory Data Analysis (EDA)
- Checked distribution of churn  
- Visualized relationship between tenure, monthly charges, and churn  

### 3. Feature Engineering
- Scaled numeric features using `StandardScaler`  
- Prepared train-test split (80% / 20%)  

### 4. Model
- **Algorithm:** Logistic Regression  
- **Accuracy:** 82%  
- Evaluated with **Confusion Matrix**, **Classification Report**  

### 5. Streamlit App
- Input customer details: tenure, monthly charges, total charges  
- Output: churn prediction, probability, top factors influencing churn  


## **Folder Structure**
customer-churn-app/
│
├── app.py # Streamlit app
├── model.pkl # Trained model
├── scaler.pkl # Scaler for numeric features
├── features.pkl # Feature column names
├── requirements.txt # Required Python libraries
└── README.md # Project documentation

## Run the Code**
**Deploy on Streamlit Cloud:**
- Push all files to GitHub  
- Go to [Streamlit Cloud](https://share.streamlit.io/)  
  - Click **New App**  
  - Select your repository, branch, and `app.py` as main file  
  - Click **Deploy** → your app is live  

## ** Insights from Model**
- Customers with **month-to-month contracts** or **high monthly charges** are more likely to churn  
- **Long tenure** and **loyalty services** reduce churn probability  
- Feature importance helps **identify reasons behind churn**  

## **Learning Outcomes**
- Practiced full **Data Science workflow**  
- Built a **Logistic Regression model** from scratch  
- Learned to **deploy ML models with Streamlit**  
- Gained experience in **EDA, feature engineering, and model evaluation**  

## **Technologies Used**
- Python  
- Pandas, NumPy  
- Scikit-learn  
- Matplotlib, Seaborn  
- Streamlit

