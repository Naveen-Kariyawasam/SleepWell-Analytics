import streamlit as st
import joblib
import numpy as np
import pandas as pd
import requests
from sklearn.preprocessing import LabelEncoder
from streamlit_lottie import st_lottie

path_to_model = 'best_random_forest_model.joblib'

with open(path_to_model, 'rb') as file:
    model = joblib.load(file)

feature_names = joblib.load('./feature_names.pkl')
 
#Load the label encoders for categorical columns
label_encoders = {
    'Gender': joblib.load('Gender_label_encoder.pkl'),
    'Occupation': joblib.load('Occupation_label_encoder.pkl'),
    'BMI Category': joblib.load('BMI_Category_label_encoder.pkl'),
    'Blood Pressure': joblib.load('Blood_Pressure_label_encoder.pkl'),
    'Sleep Disorder': joblib.load('Sleep_Disorder_label_encoder.pkl')
}

# List of features (should match the model training order)
feature_names = [
    'Age', 'Gender', 'Occupation', 'Hours of Sleep', 'Physical Activity Level',
    'BMI Category', 'Blood Pressure', 'Sleep Disorder'
]

# Function to load animations for UI
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

