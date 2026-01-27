import streamlit as st
#!pip install streamlit
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

st.markdown("""
<style>
    /* Background styling */
    .stApp {background: linear-gradient(135deg, #1e1e2f 0%, #2b2b45 100%);

        background-attachment: fixed;
    }
    
    /* Title styling */
    .main-title {
        text-align: center;
        color: white;
        font-size: 2.5rem;
        font-weight: bold;
        padding: 1rem;
        background: rgba(0, 0, 0, 0.3);
        border-radius: 10px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(90deg, #1e3a8a, #3b82f6);
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        padding: 0.8rem 2rem;
        font-size: 1rem;
    }
    
    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        color: white !important;
    }
    
    /* Text color */
    .stMarkdown, .stText {
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">💧 Hydration Predictor</div>', unsafe_allow_html=True)

data = pd.read_csv('Daily_Water_Intake.csv')
st.write("What is Your Age")
age=st.select_slider("Age", options=data['Age'].unique(), key='age_slider')
st.write("What is Your Gender")
gender=st.select_slider("Gender", options=data['Gender'].unique(), key='gender_slider')
st.write("What is Your Weight")
weight=st.select_slider("Weight", options=data['Weight (kg)'].unique(), key='weight_slider')
hydrate={
    'Good':1,
    'Poor':2,
    'Moderate':3
}


data['Hydration Level']=data['Hydration Level'].map(hydrate)
st.write("How much Hydrated do you Feel ?")
hydrated=st.select_slider("hydration-Level", options=data['Hydration Level'].unique(), key="Hydration Level")
data['Gender']=data['Gender'].map({'Male':0,'Female':1})

data['Gender'] = data['Gender'].fillna(2)

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split # Ensure this import is present
from sklearn.linear_model import LinearRegression # Import LinearRegression for regression task
features=["Age","Gender","Weight (kg)","Hydration Level"]
x=data[features]
y=data['Daily Water Intake (liters)']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model=LinearRegression() 
model.fit(x_train,y_train)
gender_mapping_for_prediction = {'Male':0, 'Female':1}

numerical_gender = gender_mapping_for_prediction.get(gender, 2) 


input_data_df = pd.DataFrame([[age, numerical_gender, weight, hydrated]],
                             columns=features) 
st.markdown("---")
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader(" Make Prediction")
st.write("Your water intake must be around:")


if st.button("Predict"):
    predicted_litre_intake = model.predict(input_data_df)
    st.write(f"{predicted_litre_intake[0]:.2f} liters")
st.markdown('</div>', unsafe_allow_html=True)