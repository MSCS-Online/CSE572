#!/usr/bin/env python3

"""Jeremy Escobar, Spring session B, CSE 572"""

import pandas as pd
import numpy as np
from sklearn import decomposition, preprocessing, model_selection
from sklearn.tree import DecisionTreeClassifier
from scipy.fftpack import fft
import pickle


def load_data():
    """Load the data from the csv files"""
    insulin_dataframe = pd.read_csv(
        "InsulinData.csv", low_memory=False
    )  # Load the insulin data
    insulin_patient = pd.read_csv(
        "Insulin_patient2.csv", low_memory=False
    )  # Load the insulin patient data
    glucose_dataframe = pd.read_csv("CGMData.csv", low_memory=False)  # Load the glucose data
    glucose_patient = pd.read_csv(
        "CGM_patient2.csv", low_memory=False
    )  # Load the glucose patient data
    return (
        insulin_dataframe,
        insulin_patient,
        glucose_dataframe,
        glucose_patient,
    )  # Return the dataframes


def identify_time_intervals(intervals, delta):
    """Identify the time intervals between the insulin data"""
    pass


def preprocess_and_extract(insulin_dataframe, glucose_dataframe):
    pass:


def create_dataframe_from_intervals():
    pass


def extract_features(df):
    """Extract the features from the dataframe"""
    pass


def calculate_features(data):
    """Calculate the features from the data"""
    pass


def train_and_save_model(X, y):
    """Train and save the model"""
    pass


def main():
    """Main function"""
    


if __name__ == "__main__":
    main()
