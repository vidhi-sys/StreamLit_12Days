# !pip install streamlit
import pandas as pd
import streamlit as st
from PIL import Image
import datetime
image=Image.open("mood.png")
st.image(image)
st.write("""
# Mood Tracker
This App aligns your Mood and builds you a Weekly/Daily Mood Board
***

""")
# *** is the hr tag
# enter Mood)
st.header("Your Mood Today ? ")
sample_input="Happy"
mood_input = st.text_area("Enter your mood here:", height=100, value=sample_input)
mood = "calm"
mood_color = "#A8DADC"
explanation = "Soft greens and blues are associated with emotional balance and calmness."

text = mood_input.lower()

# Mood detection (IMPORTANT: elif)
if "tired" in text or "exhausted" in text:
    mood = "tired"
    mood_color = "#B7B7A4"
    explanation = "Muted earthy tones reflect low energy and the need for rest."
elif "happy" in text or "excited" in text:
    mood = "happy"
    mood_color = "#FFD93D"
    explanation = "Yellow represents optimism, warmth, and positive emotional energy."
elif "sad" in text or "depressed" in text:
    mood = "sad"
    mood_color = "#6B728E"
    explanation = "Cool muted blues reflect introspection and emotional depth."
elif "calm" in text or "peaceful" in text:
    mood = "calm"
    mood_color = "#A8DADC"
    explanation = "Soft teal tones reduce stress and promote emotional grounding."
elif "anxious" in text or "worried" in text:
    mood = "anxious"
    mood_color = "#2D2A32"
    explanation = "Dark neutral tones represent tension and mental overload."

# Date
today = datetime.date.today().strftime("%d %B %Y")
st.caption(f" Your mood color for {today}")

# SINGLE COLOR SHEET (THIS IS THE MAIN PART)
st.markdown(
    f"""
    <div style="
        background-color:{mood_color};
        height:260px;
        border-radius:25px;
        margin-top:25px;
        display:flex;
        align-items:center;
        justify-content:center;
        font-size:26px;
        font-weight:600;
        color:#111;
    ">
        {mood.upper()} · {mood_color}
    </div>
    """,
    unsafe_allow_html=True
)

# Explanation
st.markdown("###  Why this color?")
st.write(explanation)