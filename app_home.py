import pandas as pd
import streamlit as st
from PIL import Image


def run_home_app():
    st.title('인천광역시 의료기관')
    img=Image.open('./data/host1.jpg')
    st.image(img)