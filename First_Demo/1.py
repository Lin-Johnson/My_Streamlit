import streamlit as st
import numpy as np
import pandas as pd
import time
import os

path_to_find = os.listdir()
st.title(path_to_find)

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()

df = pd.read_excel("https://github.com/Lin-Johnson/My_Streamlit/edit/main/First_Demo/Streamlit_Demo.xlsx")
chart_data = df.loc[:,['高温(℃)','低温(℃)']]
chart_data.index = df['2022年月份']
chart = st.line_chart(chart_data)

progress_bar.empty()


# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
