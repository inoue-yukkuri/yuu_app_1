import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/yasai0228.csv', index_col='yasai')
st.dataframe(df)
st.bar_chart(df['N'])

fig, ax =plt.subplots()
ax.plot(df.index,df['N'])
st.pyplot(fig)