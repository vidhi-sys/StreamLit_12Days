#!pip install streamlit
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv('delivery_data.csv')
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import streamlit as st
st.header("Welcome to 🍅 TOMATO (Zomato Spoof)")
st.write("Predict whether an order will be delayed or not")
delivery_rating=st.radio("Delivery Agent Rating",[1,2,3,4,5])
distance=st.slider("Distance(km)", min_value=10, max_value=100)
hour=st.slider("Hour", min_value=1, max_value=24)
X = data[["distance_km", "partner_rating", "hour_of_day"]]
y = data["delayed"]

model = LogisticRegression()
model.fit(X, y)
input_data = np.array([[distance, delivery_rating, hour]])
delay_prob = model.predict_proba(input_data)[0][1]
if st.button("Predict"):
    if delay_prob > 0.6:
        delay = True
        st.error("🍅 Tomato says sorry 😔 —> high delay risk")
    else:
        delay = False
        st.success("🍅 Tomatolicioussss 😋 —> delivery looks smooth")

    st.write("Delay flag:", delay)
