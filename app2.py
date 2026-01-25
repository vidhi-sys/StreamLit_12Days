import streamlit as st
import pandas as pd
df=pd.read_csv('IPL2025Batters.csv')
df = df[['Player Name', 'Runs']]
st.write(""" 
# IPL-2026
Simple Predictor App using StreamLit""")
st.line_chart(df, x='Player Name', y='Runs')
st.bar_chart(df, x='Player Name', y='Runs')
st.scatter_chart(df, x='Player Name', y='Runs',color='#FFC0CB')