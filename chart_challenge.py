from typing import Union, Any
import pandas as pd
import plotly.express as px
import streamlit as st
from plotly.graph_objs import Figure
from PIL import Image

@st.cache
def get_data():
    return pd.read_csv(
        "https://docs.google.com/spreadsheets/d/e/2PACX-1vSzU-mcl6RIJjzLjSut1nNd1pN2QEjx-8L7gzAqM-d6n-kZb-dLDE-YbkjFxP65Wx_Eweaax901jrd3/pub?gid=1490223003&single=true&output=csv")


df = get_data()

st.title("📊 #30DayChartChallenge 2022 Day 14: 3 dimensional 📈")
st.markdown(
    "I could have shared a static image only, but then y'all wouldn't have seen the super cool interactivity of Plotly Express's 3-D scatterplot. \n"
    "You can zoom in, out, pan around the view, and see each mark from all angles. Hover to view tooltips. \n"
    "This data is from the 2021 Data Visualization Society State of the Industry Survey.")


image = Image.open('DVSlogo.png')
st.image(image)


st.markdown(">This is my favorite part about analytics: Taking boring flat data and bringing it to life through visualization \n\n—John Tukey")

fig = px.scatter_3d(df, x="Number of charts used in production (last 6 months)", y='Number of data visualization tools', z='Number of channels used for sharing visualizations',
              color="Number of charts used in production (last 6 months)", labels={
                     "Number of data visualization tools": "Number of tools",
                     "Number of charts used in production (last 6 months)": "Number of charts",
                     "Number of channels used for sharing visualizations": "Number of channels"}, color_continuous_scale = "darkmint",
                   title="The number of tools, chart types, and channels for sharing used by data visualization practitioners")

st.write(fig)

st.markdown("Check out my [new website](https://www.nicoledesignsdata.com)")

st.write("You know you want to click that button 👇🏼")
btn = st.button("Celebrate!")
if btn:
    st.balloons()
