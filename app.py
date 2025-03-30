import streamlit as st
import pandas as pd
from joblib import load

# Load the AdaBoost model
ada_classifier = load('ada_boost_model.joblib')

# Expected feature names during model training
expected_columns = [
    'age', 'hypertension', 'heart_disease', 'bmi', 'HbA1c_level',
    'blood_glucose_level', 'smoking_history_ever', 'smoking_history_former',
    'smoking_history_never', 'smoking_history_not current'
]

# Add custom styles for a colorful UI
st.markdown(
    """
    <style>
    .main-title {
        color: #4CAF50;
        font-family: Arial, sans-serif;
        text-align: center;
        font-size: 40px;
        margin-bottom: 20px;
        border-bottom: 3px solid #4CAF50;
    }
    .header {
        color: #2196F3;
        font-family: Verdana, sans-serif;
        font-size: 28px;
    }
    .form-section {
        background-color: #f9f9f9;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    }
    .submit-btn {
        background-color: #FF5722;
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 5px;
        padding: 10px 15px;
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit app
st.markdown('<h1 class="main-title">Diabetes Prediction App</h1>', unsafe_allow_html=True)

# Form to take input from the user
st.markdown('<h2 class="header">Enter Patient Details:</h2>', unsafe_allow_html=True)

age = st.number_input("Age (years)", min_value=0, max_value=120, step=1)
hypertension = st.selectbox("Hypertension (High Blood Pressure)", options=["Yes", "No"])
heart_disease = st.selectbox("Heart Disease", options=["Yes", "No"])
bmi = st.number_input("BMI (Body Mass Index)", min_value=0.0, format="%.2f")
hba1c = st.number_input("HbA1c Level (%)", min_value=0.0, format="%.1f")
blood_glucose = st.number_input("Blood Glucose Level (mg/dL)", min_value=0.0, format="%.1f")
smoking_history = st.selectbox(
    "Smoking History", options=["Ever", "Former", "Never", "Not Current"]
)

st.markdown('</div>', unsafe_allow_html=True)

# Button to make predictions
if st.button("Predict Diabetes"):
    # Map smoking history to match expected columns
    smoking_mapping = {
        "Ever": [1, 0, 0, 0],
        "Former": [0, 1, 0, 0],
        "Never": [0, 0, 1, 0],
        "Not Current": [0, 0, 0, 1],
    }
    smoking_values = smoking_mapping[smoking_history]

    # Preprocess the input data
    data = {
        'age': [age],
        'hypertension': [1 if hypertension == "Yes" else 0],
        'heart_disease': [1 if heart_disease == "Yes" else 0],
        'bmi': [bmi],
        'HbA1c_level': [hba1c],
        'blood_glucose_level': [blood_glucose],
        'smoking_history_ever': [smoking_values[0]],
        'smoking_history_former': [smoking_values[1]],
        'smoking_history_never': [smoking_values[2]],
        'smoking_history_not current': [smoking_values[3]],
    }
    input_data = pd.DataFrame(data)

    # Align columns with the expected order
    for col in expected_columns:
        if col not in input_data.columns:
            input_data[col] = 0  # Add missing columns with default value
    input_data = input_data[expected_columns]  # Reorder columns to match the model

    # Make predictions using the AdaBoost model
    try:
        prediction = ada_classifier.predict(input_data)

        # Output results
        if prediction[0] == 1:
            st.success("The patient is likely to have diabetes.")
        else:
            st.success("The patient is not likely to have diabetes.")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")