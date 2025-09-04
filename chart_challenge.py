import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

@st.cache_data
def get_data():
    return pd.read_csv("dvs_survey_data.csv")


df = get_data()

st.title("📊 #30DayChartChallenge 2022 Day 14: 3 dimensional 📈")
st.markdown(
    "I could have shared a static image only, but then y'all wouldn't have seen the super cool interactivity of Plotly Express's 3-D scatterplot. \n"
    "You can zoom in, out, pan around the view, and see each mark from all angles. Hover to view tooltips. \n"
    "This data is from the 2021 Data Visualization Society State of the Industry (SOTI) Survey. Learn more and see the full \n"
    "dataset [here](https://www.datavisualizationsociety.org/survey).")

image = Image.open('DVSlogo.png')
st.image(image, width =250, use_column_width=False)

st.markdown("*This is my favorite part about analytics: Taking boring flat data and bringing it to life through visualization.* \n\n—John Tukey")

st.subheader("The interactive plot below explores respondents' answers to the following three questions from the SOTI survey:")
st.markdown("- Q34. What technologies do you use often to visualize data? The number of tools the respondent selected is represented on the axis labeled **Number of tools**. \n"
"- Q35. Which of these charts have you used in production in the last 6 months? The number of charts the respondent selected is represented on the axis labeled **Number of charts**. \n"
"- Q36. How do you communicate your data visualizations? The number of communication channels the respondent selected is represented on the axis labeled **Number of channels**.")

fig = px.scatter_3d(df, x="Number of charts used in production (last 6 months)", y='Number of data visualization tools', z='Number of channels used for sharing visualizations',
              color="Number of charts used in production (last 6 months)", labels={
                     "Number of data visualization tools": "Number of tools",
                     "Number of charts used in production (last 6 months)": "Number of charts",
                     "Number of channels used for sharing visualizations": "Number of channels"}, color_continuous_scale = "darkmint",
                   title="The number of tools, chart types, and channels for sharing used by data visualization practitioners")

st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

st.markdown("Check out my [new website](https://www.nicoledesignsdata.com)!")

st.write("You know you want to click that button 👇🏼")
btn = st.button("Celebrate!")
if btn:
    st.balloons()
