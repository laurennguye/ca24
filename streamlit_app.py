import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Streamlit Setup and User Interaction
st.title("My First Streamlit App")
st.write("This app demonstrates simple user interactions and data visualization.")

# 2. User Input Controls
name = st.text_input("Enter your name:")
age = st.slider("Select your age:", 1, 100, 25)

if name:
    st.write(f"Hello, {name}!")
st.write(f"You are {age} years old.")

# 3. Button Interaction
if st.button("Say hello"):
    st.write("Hello there!")

# 4. Data Manipulation and Display
data = {'Name': ['John', 'Jane', 'Jake', 'Jill'], 'Age': [28, 24, 32, 29]}
df = pd.DataFrame(data)
st.write("Sample DataFrame:")
st.dataframe(df)

# 5. Data Visualization
st.write("Age Histogram:")
fig, ax = plt.subplots()
ax.hist(df['Age'], bins=5)
st.pyplot(fig)
