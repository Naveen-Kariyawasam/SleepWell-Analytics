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

