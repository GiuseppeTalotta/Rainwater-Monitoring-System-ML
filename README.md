# Rainwater Monitoring System with Machine Learning

## Overview
This project presents a sensor-based system to monitor rainwater quality for agricultural use. It integrates multiple sensors to measure parameters such as pH and electrical conductivity and uses a machine learning model to automatically classify water quality as suitable or not for irrigation.

## Features
- Real-time sensor data acquisition (pH, conductivity, etc.)
- Machine Learning model (Random Forest) to predict water quality
- User-friendly web interface built with Streamlit
- Supports manual input and CSV file upload for batch prediction
- Visualizations including scatter plots and bar charts to analyze data distribution

## Machine Learning Component
The system includes a supervised machine learning model trained to classify rainwater quality based on pH and conductivity values. The Random Forest classifier was selected for its robustness with small datasets and noisy data.

The trained model (`model.pkl`) is loaded in the Streamlit app (`app.py`) to provide real-time predictions through:
- Manual input mode: users input values to get immediate feedback
- CSV upload mode: users can upload datasets for batch classification and visualization

## Installation
To run the project locally, first clone the repository:

```bash
git clone https://github.com/GiuseppeTalotta/Rainwater-Monitoring-System-ML.git
cd Rainwater-Monitoring-System-ML
