
# 🚗 Car Price Prediction App

![Car Price Prediction](https://img.shields.io/badge/Car%20Price%20Prediction-App-brightgreen) 
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-green?style=flat-square&logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployment-orange?style=flat-square&logo=streamlit)

Welcome to the **Car Price Prediction App**! This web application helps users predict the price of a used car based on its features. It uses machine learning to forecast the price and allows users to explore and filter cars interactively.

---

![Screenshot (58)](https://github.com/user-attachments/assets/08d4e4ab-567c-4b03-aa64-3871bcf3e2dd)

## ✨ Project Highlights

---

**Feature**                     | **Details**
------------------------------ | ------------------------------------------------------------------------
**Data Cleaning & Preprocessing**| Organized and structured data from various cities with thorough data cleaning.
**Exploratory Data Analysis**   | In-depth analysis to identify patterns, relationships, and influential features.
**Machine Learning Models**     | Trained multiple regression models (Linear Regression, Decision Trees, Random Forest, etc.) to predict prices.
**Model Evaluation**            | Used metrics like MAE, MSE, and R-squared, with hyperparameter tuning for optimal performance.
**Streamlit Deployment**       | Developed an interactive application for real-time car price predictions.

---

## 🔧 Tools and Technologies

- ![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
- ![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black?style=flat-square&logo=pandas)
- ![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-green?style=flat-square&logo=scikitlearn)
- ![Streamlit](https://img.shields.io/badge/Streamlit-Deployment-orange?style=flat-square&logo=streamlit)
- ![Joblib](https://img.shields.io/badge/Joblib-v1.1.0-blue)

---

## 📊 **Project Overview**

The **Car Price Prediction App** predicts the price of used cars based on various features such as:
- Year of Manufacture
- Mileage
- Engine Capacity
- Power
- Seats
- Fuel Type
- Transmission Type

The app also provides a dataset explorer to filter cars by price range, fuel type, and brand.

---

## 🚀 **Features**

- **Interactive Filters**: Filter cars based on price, fuel type, and brand.
- **Price Prediction**: Input car features and predict the price of a used car.
- **Data Exploration**: View a dataset of used cars with various features, and explore how car price correlates with different factors.
- **Visualizations**: Interactive scatter plots that help understand the relationship between car price and features such as mileage, engine capacity, and power.

---


## 📈 **How It Works**

The **Car Price Prediction App** uses a **Gradient Boosting Model** to predict car prices. This model was trained on a dataset containing various features of used cars such as `Year of Manufacture`, `Mileage`, `Engine Capacity`, `Power`, etc.

### **Flow of the App**:

1. **Predict Price**: Enter the car details, and the model will predict the price.
2. **Explore Cars**: Use the sidebar to filter cars by price, fuel type, and brand.
3. **Visualizations**: Interact with charts to explore relationships between car features and prices.

---

## 🧰 **How to Run the App Locally**

### **Requirements**

- Python 3.8 or higher
- Libraries: python,scikit-learn,Streamlit, Pandas,numpy,Plotly, Joblib, etc.

### **Steps**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/car-price-prediction-app.git
   cd car-price-prediction-app

2. **Install requirements.txt and run app:**

   ```
   pip install -r requirements.txt

   streamlit run app.py

