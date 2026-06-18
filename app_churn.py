import streamlit as st
import pandas as pd
import numpy as np
import pickle


# LOAD MODEL

model, scaler, features = pickle.load(open("churn_model.pkl", "rb"))

st.title("📊 Customer Churn Prediction System")

st.write("Enter Customer Details:")


# USER INPUTS

age = st.slider("Age", 18, 80, 30)
gender = st.selectbox("Gender", ["Male", "Female"])

income = st.number_input("Income", 1000, 100000, 30000)
spending = st.slider("Spending Score", 1, 100, 50)
purchase = st.number_input("Purchase Amount", 100, 10000, 500)

product = st.selectbox("Product Category", ["Electronics", "Clothing", "Grocery"])
payment = st.selectbox("Payment Method", ["Cash", "Card", "UPI"])

city = st.selectbox("City", ["Bangalore", "Chennai", "Delhi"])
state = st.selectbox("State", ["Karnataka", "Tamil Nadu", "Delhi"])
country = st.selectbox("Country", ["India", "USA", "UK"])

returns = st.slider("Returns", 0, 10, 1)
discount = st.slider("Discount Used", 0, 5, 1)
review = st.slider("Review Score", 1, 5, 3)

browser = st.selectbox("Browser", ["Chrome", "Safari", "Edge"])
device = st.selectbox("Device", ["Mobile", "Desktop"])

session = st.slider("Session Time", 1, 60, 10)

# CREATE INPUT DATAFRAME

input_dict = {
    'Age': age,
    'Gender': gender,
    'Income': income,
    'SpendingScore': spending,
    'PurchaseAmount': purchase,
    'ProductCategory': product,
    'PaymentMethod': payment,
    'City': city,
    'State': state,
    'Country': country,
    'Returns': returns,
    'DiscountUsed': discount,
    'ReviewScore': review,
    'Browser': browser,
    'Device': device,
    'SessionTime': session
}

input_df = pd.DataFrame([input_dict])


# APPLY SAME PREPROCESSING AS TRAINING

# One-hot encoding
input_df = pd.get_dummies(input_df)

# Add missing columns
for col in features:
    if col not in input_df.columns:
        input_df[col] = 0

# Ensure same order
input_df = input_df[features]


# SCALING
input_scaled = scaler.transform(input_df)

# PREDICTION

if st.button("Predict"):
    pred = model.predict(input_scaled)
    result = "Churn" if pred[0] == 1 else "Not Churn"
    st.success(f"Prediction: {result}")