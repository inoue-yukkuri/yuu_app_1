import streamlit as st
from PIL import Image

st.title('ゆっくりアプリ')
st.caption('テストアプリです') 

image=Image.open('./data/25309121_m.jpg')
st.image(image, width=200)