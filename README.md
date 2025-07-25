# Rainwater Monitoring System with Machine Learning

This project presents a simple and intelligent system designed to evaluate the quality of collected rainwater through a web application. The main goal is to automatically classify rainwater as **"Good"** or **"Not Good"** for irrigation purposes, using two key parameters: **pH** and **Electrical Conductivity (EC)**.

## 🧠 Machine Learning Component

A supervised **Random Forest classifier** was trained using Python and `scikit-learn`. The dataset was artificially created for prototyping and consists of realistic pH and EC values with binary labels indicating water quality. The trained model is saved as `model_acqua.pkl` using `joblib`.

### 📁 Main Files

- `train_model.py`: script for training the model.
- `model_acqua.pkl`: trained model.
- `app.py`: web app interface built with Streamlit.
- `requirements.txt`: list of dependencies.

## 🌐 Web Application (Streamlit)

The app offers two usage modes:

1. **Manual Input**: Users can enter pH and EC values via number input fields. A prediction will be shown with a clear message and icon.
2. **CSV Upload**: Users can upload a CSV file with multiple rows of values. The app returns a prediction table and two visualizations:
   - Scatter Plot (pH vs EC)
   - Bar Chart (Good vs Not Good predictions)

## 🖼️ Interface Features

- Clean and user-friendly layout
- Icons and color-coded feedback
- Author info section at the bottom

## 📦 Requirements

Install required libraries:

pip install -r requirements.txt

## 🔧 How to Run Locally

streamlit run app.py

## 📘 About the Author

Developed by Giuseppe Talotta as part of a thesis project for the Biomedical and Computer Engineering degree at Università Magna Graecia di Catanzaro.

The app demonstrates how machine learning and IoT-based environmental monitoring can be combined to build practical, low-cost tools for agriculture and education.
