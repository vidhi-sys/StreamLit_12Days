import streamlit as st
import numpy as np
import pandas as pd
import joblib
from tensorflow.keras.models import load_model

st.set_page_config(page_title="Customer Churn Predictor")

# Load assets
model = load_model("churn_model.h5")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

cols_toscale = ['tenure', 'TotalCharges', 'MonthlyCharges']

st.title(" Customer Churn Predictor")

tenure = st.slider("Tenure (months)", 0, 72, 12)
monthly = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
total = st.number_input("Total Charges", 0.0, 10000.0, 2000.0)
gender = st.selectbox("Gender", ["Male", "Female"])

gender_val = 1 if gender == "Female" else 0

# Build input row
input_dict = {col: 0 for col in columns}
input_dict["tenure"] = tenure
input_dict["MonthlyCharges"] = monthly
input_dict["TotalCharges"] = total
input_dict["gender"] = gender_val

input_df = pd.DataFrame([input_dict])
input_df[cols_toscale] = scaler.transform(input_df[cols_toscale])

if st.button("Predict Churn"):
    prob = model.predict(input_df, verbose=0)[0][0]
    st.metric("Churn Probability", f"{prob*100:.2f}%")

    if prob > 0.5:
        st.error("⚠️ High chance of churn")
    else:
        st.success("✅ Customer likely to stay")
