import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Title
st.title("Car MSRP Visualization by Brand")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('CARS.csv')
    df['MSRP'] = df['MSRP'].str.replace('[$,]', '', regex=True).astype('int64')
    return df

df = load_data()

# Brand Selection
brands = df['Make'].unique()
selected_brand = st.selectbox("Select a Car Brand:", sorted(brands))

# Filtered Data
brd = df[df['Make'] == selected_brand]

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
sb.barplot(x=brd['Model'], y=brd['MSRP'], ax=ax)
plt.xticks(rotation=90)
plt.title(f'MSRP of {selected_brand} Models')
plt.ylabel("MSRP ($)")
plt.xlabel("Model")

st.pyplot(fig)
