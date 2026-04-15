import streamlit as st
import pandas as pd

st.title("Streamlit Text input")
name = st.text_input("Enter your name:")

# slider
age = st.slider("select your age:",0,100,25)
st.write(f"Your age is {age}.")

#
options = ["Python","Java","C++","Javascript"]
choice = st.selectbox("choose your favorite language:", options)
st.write(f"your selected {choice}.")
if name:
  st.write(f"Hello, {name}")

# dataframes
data = {
  "name" : ["jhon","jane","jake","jill"],
  "age"  : [28,24,35,40],
  "city" : ["New York", "Los Angles", "Chicago","Houston"]
}
df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)


# upload button
uploaded_file = st.file_uploader("choose a CSV file",type="csv")

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.write(df)

## visit streamliot.io  