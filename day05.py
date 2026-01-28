#!pip install streamlit

import streamlit as st
import pandas as pd
import cv2 as cv
from PIL import Image
st.title("Food Freshness Level")
st.caption("Lets Check How Fresh is Your Food?")
uploaded_file = st.file_uploader("Upload a food image", type=["jpg", "png", "jpeg"])
import numpy as np
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image)
    img=np.array(image)
    img_resize=cv.resize(img,(224,224))
    st.image(img, caption="Uploaded Image", use_container_width =True)
    img_bgr=cv.cvtColor(img_resize,cv.COLOR_RGB2BGR)
    img_rich=cv.cvtColor(img,cv.COLOR_RGB2HSV)
    richness=img_rich[:,:,2].mean()
    img_sharp=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
    sharpness=cv.Laplacian(img_sharp,cv.CV_64F).var()
    _, thresh = cv.threshold(img_sharp, 60, 255, cv.THRESH_BINARY_INV)
    contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    dark_spots = len(contours)

    fresh=0
    if richness>80:
      fresh+=1
    if sharpness>100:
      fresh+=1
    if dark_spots<150:
      fresh+=1

    st.write(f"### Freshness Score: {fresh}/3")
    if fresh == 3:
        st.success("Your food appears to be very fresh!")
    elif fresh >= 1:
        st.warning("Your food might be moderately fresh. Consider checking it closely.")
    else:
        st.error("Your food might not be fresh. It's recommended to discard it.")