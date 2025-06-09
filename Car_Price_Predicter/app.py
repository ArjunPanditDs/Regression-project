import streamlit as st
import pandas as pd
import pickle
from PIL import Image

# --- Load Model ---
with open("LinearRegressionMOdel.pkl", "rb") as f:
    pipe = pickle.load(f)

# --- Load Data for Dropdowns ---
df = pd.read_csv("Cleaned_car.csv")  # Your full dataset

# --- Streamlit Page Setup ---
st.set_page_config(page_title="Car Price Predictor", page_icon="🚗", layout="centered")

# --- Custom CSS ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    .stButton > button {
        background-color: #0072ff;
        color: white;
        padding: 0.6rem 1rem;
        border-radius: 5px;
        border: none;
        font-weight: 600;
    }
    .stButton > button:hover {
        background-color: #005ce6;
        transition: 0.3s ease;
    }
    .stTitle {
        text-align: center;
        color: #0072ff;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title and Header Image ---
st.title("🚗 Car Price Prediction Engine")
st.subheader("Enter your car details below to know its worth 🔍")

# --- Main Form Container ---
with st.container():
    with st.form(key='car_form'):
        st.markdown("### 🧾 Car Details")

        col1, col2 = st.columns(2)
        with col1:
            name = st.selectbox("Car Model", sorted(df['name'].unique()))
            year = st.selectbox("Year of Purchase", sorted(df['year'].unique(), reverse=True))
        with col2:
            company = st.selectbox("Manufacturer", sorted(df['company'].unique()))
            fuel_type = st.selectbox("Fuel Type", sorted(df['fuel_type'].unique()))

        kms_driven = st.slider("Kilometers Driven", 0, 200000, step=1000)

        # Submit
        submit = st.form_submit_button(label='Predict Price')

    # --- Prediction ---
    if submit:
        input_data = pd.DataFrame([[name, company, year, kms_driven, fuel_type]],
                                  columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])

        predicted_price = pipe.predict(input_data)[0]
        st.success(f"💰 Estimated Car Price: ₹ {int(predicted_price):,}")

        # Optional Bonus Styling
        st.markdown("""
            <hr>
            <div style="text-align:center;">
                <h4 style="color:#0072ff;">Thank you for using Car Price Predictor!</h4>
                <p style="font-size:13px;">Drive safe and stay classy 🛣️</p>
            </div>
        """, unsafe_allow_html=True)
