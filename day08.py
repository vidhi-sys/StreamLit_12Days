import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.header("Doodle Tool ")

drawing_mode = st.sidebar.selectbox(
    "Drawing tool:",
    ("point", "freedraw", "line", "rect", "circle", "transform")
)

stroke_width = st.sidebar.slider("Stroke width:", 1, 25, 3)
stroke_color = st.sidebar.color_picker("Stroke color:", "#000000")

canvas_result = st_canvas(
    background_color="rgb(192, 194, 201)",
    height=300,
    width=900,
    stroke_color=stroke_color,
    stroke_width=stroke_width,
    drawing_mode=drawing_mode,
    key="canvas",
)
