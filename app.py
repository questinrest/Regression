import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load your trained model
model = joblib.load('your_model.pkl')

# Function to predict price
def predict_price(carat, cut, color, clarity):
    # Convert categorical inputs to numerical
    cut_num = {"Fair": 0, "Good": 1, "Very Good": 2, "Premium": 3, "Ideal": 4}[cut]
    color_num = {"J": 0, "I": 1, "H": 2, "G": 3, "F": 4, "E": 5, "D": 6}[color]
    clarity_num = {"I1": 0, "SI2": 1, "SI1": 2, "VS2": 3, "VS1": 4, "VVS2": 5, "VVS1": 6, "IF": 7}[clarity]

    # Make prediction
    features = np.array([[carat, cut_num, color_num, clarity_num]])
    price = model.predict(features)[0]
    return price

# App layout
st.title('Gemstone Price Prediction')

carat = st.number_input('Carat', min_value=0.2, max_value=5.01, value=0.5, step=0.01)
cut = st.selectbox('Cut', ("Fair", "Good", "Very Good", "Premium", "Ideal"))
color = st.selectbox('Color', ("J", "I", "H", "G", "F", "E", "D"))
clarity = st.selectbox('Clarity', ("I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"))

if st.button('Predict'):
    try:
        price = predict_price(carat, cut, color, clarity)
        st.success(f'The predicted price is ${price:.2f}')
    except Exception as e:
        st.error(f'Error: {e}')
