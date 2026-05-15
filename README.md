# Used-Car-Prices-Estimator
# 🚗 Intelligent Used Car Valuation Engine (Pakistan)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)

An enterprise-grade Machine Learning web application designed to predict the fair market value of used cars in Pakistan. Built on a highly refined scraped dataset, this engine achieves a massive **97.21% R-Squared accuracy**, outperforming standard baseline models by utilizing deep variant-level data processing.

---

## 📸 Application Showcase
*(Note: Replace these with actual screenshots of your running app! You can just drag and drop the image files directly into the GitHub text editor here.)*
- **Main UI:** [Add screenshot here]
- **Prediction Result:** [Add screenshot here]

---

## 🌟 Key Features

* **High-Precision AI Model:** Powered by a `RandomForestRegressor` trained on thousands of real-world vehicle listings. Random Forest was chosen as the champion model after outperforming XGBoost and Multiple Linear Regression on sparse, high-dimensional variant data.
* **Smart Cascading UI:** Built with Streamlit, the frontend utilizes a 3-level nested dictionary (`Make -> Model -> Variant`). 
* **Factory-Spec Enforcement:** Selecting a vehicle variant automatically locks the Engine Capacity (CC), Fuel Type, and Transmission to their real-world factory specifications. This prevents users from inputting physically impossible combinations (e.g., a 1300cc Manual Hybrid), ensuring mathematically sound AI predictions.
* **Robust Data Pipeline:** - **Regex Cleansing:** Stripped user-generated noise (e.g., "8.5/10 condition", "For Sale") from raw text to unify genuine vehicle trims.
  - **Outlier Mitigation:** Domain-knowledge thresholds implemented to cap extreme mileages and impossible engine capacities.

---

## 🛠️ Tech Stack & Architecture

* **Language:** Python
* **Data Manipulation & Cleaning:** Pandas, NumPy, Regular Expressions (Regex)
* **Machine Learning:** Scikit-Learn (Random Forest, Min-Max Scaler), XGBoost (Tested & Evaluated)
* **Web Framework:** Streamlit
* **Serialization:** Joblib

---

## 📁 Project Structure
```text
📦 Used Car Prices Estimator Project
 ┣ 📜 app.py                                # The main Streamlit web application
 ┣ 📜 project.ipynb                         # Jupyter Notebook containing EDA, Cleaning, and ML Training
 ┣ 📜 random_forest_car_price_model.pkl     # The exported 97% accurate AI model
 ┣ 📜 minmax_scaler.pkl                     # Scaler to normalize numerical user inputs
 ┣ 📜 expected_columns.pkl                  # Enforces exact column order for One-Hot Encoded data
 ┣ 📜 make_model_variant_dict.pkl           # 3-level nested dictionary powering the dynamic UI
 ┗ 📜 README.md                             # Project documentation
