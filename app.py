import streamlit as st
import pandas as pd
import joblib
import numpy as np

# 1. LOAD THE EXPORTED FILES
# Loading our 97% accurate Random Forest Champion!
model = joblib.load('random_forest_car_price_model.pkl')
scaler = joblib.load('minmax_scaler.pkl')
expected_columns = joblib.load('expected_columns.pkl')
ui_dict = joblib.load('make_model_variant_dict.pkl') # The 3-Level Dictionary

# 2. UI HEADER & SETUP
st.set_page_config(page_title="Used Cars AI Valuator", page_icon="🚗", layout="wide")
st.title("🚗 Intelligent Used Car Valuation Engine")
st.write("Chosen on the basis of 97% accuracy, Random Forest AI. Select your exact vehicle specifications below.")
st.markdown("---")

# 3. DYNAMIC USER INPUTS (Cascading Dropdowns)
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Vehicle Identity")
    all_makes = sorted(list(ui_dict.keys()))
    make = st.selectbox("Car Brand (Make)", all_makes)
    
    available_models = sorted(list(ui_dict[make].keys()))
    model_name = st.selectbox("Car Model", available_models)
    
    # .keys() here because Variant is now a dictionary key itself!
    available_variants = sorted(list(ui_dict[make][model_name].keys()))
    variant = st.selectbox("Car Variant", available_variants)

# FETCH EXACT SPECS FOR THE CHOSEN VARIANT
# This dictionary contains the exact matching lists for Transmission, Fuel, and CC
specs = ui_dict[make][model_name][variant]

with col2:
    st.subheader("Vehicle Specs")
    year = st.slider("Manufacturing Year", 1990, 2026, 2018)
    mileage = st.number_input("Mileage (kms)", min_value=1, max_value=500000, value=50000, step=5000)
    
    # MAGIC: Engine CC is now a Dropdown locked to reality!
    # If a Haval H6 only comes in 1499cc and 1998cc, those are the ONLY options the user will see.
    engine_cc = st.selectbox("Engine Capacity (CC)", specs['Engine CC'])

with col3:
    st.subheader("Additional Details")
    city = st.selectbox("Registered City", ['Lahore', 'Karachi', 'Islamabad', 'Rawalpindi', 'Peshawar', 'Multan', 'Faisalabad', 'Other'])
    
    # MAGIC: Transmissions and Engine Types are also locked!
    transmission = st.selectbox("Transmission", specs['Transmission'])
    engine_type = st.selectbox("Engine Type", specs['Engine Type'])

st.markdown("---")

# 4. THE PREDICTION LOGIC

if st.button("Calculate Fair Market Price", type="primary", use_container_width=True):
    with st.spinner("Analyzing market trends..."):
        # Calculate Car Age based on the slider input
        car_age = 2026 - year
        
        # Initialize an empty dictionary with all expected columns set to 0
        input_dict = {col: 0 for col in expected_columns}
        
        # Scale the numerical features perfectly using the Phase 1 scaler
        scaled_nums = scaler.transform([[mileage, engine_cc, car_age]])
        input_dict['Mileage(kms)'] = scaled_nums[0][0]
        input_dict['Engine Capacity(CC)'] = scaled_nums[0][1]
        input_dict['Car_Age'] = scaled_nums[0][2]
        
        # Map the categorical choices (Simulating One-Hot Encoding safely)
        if f"Make_{make}" in input_dict: input_dict[f"Make_{make}"] = 1
        if f"Model_{model_name}" in input_dict: input_dict[f"Model_{model_name}"] = 1
        if f"Variant_{variant}" in input_dict: input_dict[f"Variant_{variant}"] = 1
        if f"City_{city}" in input_dict: input_dict[f"City_{city}"] = 1
        
        if transmission == 'Manual' and "Transmission_Manual" in input_dict: 
            input_dict["Transmission_Manual"] = 1
        if engine_type == 'Diesel' and "Engine Type_Diesel" in input_dict: 
            input_dict["Engine Type_Diesel"] = 1
        if engine_type == 'Hybrid' and "Engine Type_Hybrid" in input_dict: 
            input_dict["Engine Type_Hybrid"] = 1
        
        # Convert dictionary to DataFrame ensuring the exact column order
        input_df = pd.DataFrame([input_dict], columns=expected_columns)
        
        # Feed to the Random Forest model
        prediction = model.predict(input_df)[0]
        
        # Display the final prediction on screen!
        st.success(f"### 🎯 Estimated Market Value: **{prediction:,.0f} PKR**")
        st.balloons()