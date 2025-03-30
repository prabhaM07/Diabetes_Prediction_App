# Diabetes Prediction App

## Features
- User-friendly interface for inputting patient details.
- Predicts diabetes likelihood using a trained AdaBoost model.
- Responsive UI with a clean and colorful design.

## Prerequisites
Ensure you have the following installed:
- Python 3.7+
- Streamlit
- Pandas
- Joblib
- Scikit-learn (for model compatibility)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/diabetes-prediction-app.git
   cd diabetes-prediction-app
   ```

2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the App
1. Ensure that the trained AdaBoost model (`ada_boost_model.joblib`) is present in the project directory.
2. Run the Streamlit application:
   ```sh
   streamlit run app.py
   ```
3. Open the provided local URL in your browser to use the app.

## File Structure
```
/diabetes-prediction-app
│── ada_boost_model.joblib   # Pre-trained AdaBoost model
│── app.py                   # Main Streamlit application
│── requirements.txt         # Python dependencies
│── README.md                # Project documentation
```

## Expected Input Fields
- **Age:** Numeric input (0-120 years)
- **Hypertension:** Yes/No selection
- **Heart Disease:** Yes/No selection
- **BMI:** Numeric input
- **HbA1c Level:** Numeric input
- **Blood Glucose Level:** Numeric input
- **Smoking History:** Dropdown with values (Ever, Former, Never, Not Current)

## Model Prediction
- Uses an AdaBoost classifier trained on medical data.
- Outputs whether the patient is likely to have diabetes.

## Deployment (Optional)
You can deploy this app on platforms like **Streamlit Sharing**, **Heroku**, or **Render**.

Example Streamlit deployment:
```sh
streamlit run app.py
```

## Contributing
Feel free to fork this repository and submit pull requests for improvements.

## License
This project is licensed under the MIT License.

---

