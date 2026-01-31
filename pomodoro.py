import streamlit as st
import time
import os

st.header("Pomodoro Focus Timer")

def local_css(file_name):
    if os.path.exists(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load CSS
local_css("pomodoro.css")

# GIF
st.image(
    "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExYXVxanVhdGoyZHEybHY3d2N3enIwazQxMng0OWxtN2ptZjY5MzQ0aCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1zgzISaYrnMAYRJJEr/giphy.gif",
    use_container_width=True
)

minutes_duration = st.number_input(
    "Enter duration in minutes",
    min_value=1,
    value=25
)

button_start = st.button("Start")
button_stop = st.button("Stop")

timer_placeholder = st.empty()

if button_start:
    st.write("Timer started")

    # 🔊 Play sound ONCE
    st.audio(
        "gentle-rain-from-window-24548.mp3",
        format="audio/wav",
        autoplay=True
    )

    total_seconds = minutes_duration * 60

    for i in range(total_seconds):
        time.sleep(1)
        remaining = total_seconds - i - 1
        m, s = divmod(remaining, 60)
        timer_placeholder.markdown(f"## ⏳ {m:02d}:{s:02d}")

    st.success("✅ Timer finished")
