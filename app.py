import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("house_price_model.pkl")

# Page configuration
st.set_page_config(
    page_title="🏡 House Price Predictor",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar with info
st.sidebar.title("🏡 House Price Predictor")
st.sidebar.markdown("""
Predict the estimated price of your house by entering details below.  
This tool uses a trained ML model to give accurate estimates.
""")
st.sidebar.markdown("🏠🏡🏘️")

# Main title with styled header
st.markdown("""
<div style="text-align:center;">
    <h1>🏡 House Price Prediction App</h1>
    <p>Enter your house details and get an instant price estimate! 🏠💰</p>
</div>
""", unsafe_allow_html=True)

# Two-column layout for inputs
col1, col2 = st.columns(2)

with col1:
    Square_Footage = st.number_input("📏 Square Footage", min_value=100, max_value=20000, value=1500, step=50)
    Num_Bedrooms = st.number_input("🛏️ Number of Bedrooms", 1, 10, 3)
    Num_Bathrooms = st.number_input("🛁 Number of Bathrooms", 1, 10, 2)
    Year_Built = st.number_input("🏗️ Year Built", 1800, 2025, 2000)

with col2:
    Lot_Size = st.number_input("🌳 Lot Size (acres)", min_value=0.01, max_value=20.0, value=0.5, step=0.01, format="%.2f")
    Garage_Size = st.number_input("🚗 Garage Size (cars)", 0, 5, 1)
    Neighborhood_Quality = st.slider("🏘️ Neighborhood Quality", 1, 10, 5)
    



# Predict button
if st.button("💰 Predict Price"):
    input_df = pd.DataFrame([{
        "Square_Footage": Square_Footage,
        "Num_Bedrooms": Num_Bedrooms,
        "Num_Bathrooms": Num_Bathrooms,
        "Year_Built": Year_Built,
        "Lot_Size": Lot_Size,
        "Garage_Size": Garage_Size,
        "Neighborhood_Quality": Neighborhood_Quality
    }])
    
    prediction = model.predict(input_df)[0]

    # Display result with styled container
    st.markdown(f"""
    <div style="background-color:#fce5cd;padding:25px;border-radius:15px;text-align:center;">
        <h2 style="color:#d35400;">💵 Estimated House Price:</h2>
        <h1 style="color:#e67e22;">${prediction:,.2f}</h1>
    </div>
    """, unsafe_allow_html=True)

# Interactive charts section
st.markdown("---")
st.subheader("🏠 House Feature Comparison")

# Sample comparison chart using user input
features = ['Square Footage', 'Bedrooms', 'Bathrooms', 'Lot Size', 'Garage Size', 'Neighborhood Quality']
values = [Square_Footage, Num_Bedrooms, Num_Bathrooms, Lot_Size, Garage_Size, Neighborhood_Quality]

chart_data = pd.DataFrame({
    'Feature': features,
    'Value': values
})

st.bar_chart(chart_data.set_index('Feature'))

