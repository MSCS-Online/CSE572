#!/usr/bin/env python3

"""Jeremy Escobar, Spring session B, CSE 572"""

import pandas as pd


def load_data(file, columns=None, date_time_combine=False):  # Load data from file
    data = pd.read_csv(file, low_memory=False, usecols=columns)  # Read data from file
    if (
        date_time_combine and "Date" in data and "Time" in data
    ):  # Combine date and time columns into a single datetime column
        data["date_time_stamp"] = pd.to_datetime(
            data["Date"] + " " + data["Time"]
        )  # Combine date and time into a single column
        data = data.drop(
            columns=["Date", "Time"]
        )  # Drop the date and time columns after combining them
    return data


def preprocess_data():
    pass


def compute_metrics():
    pass


"""
From the Continuous Glucose Sensor (CGMData.csv) 
From the insulin pump (InsulinData.csv)
"""

"""
Each of the metrics mentioned above is extracted in three different time intervals: 
daytime (6 am to midnight), 
overnight (midnight to 6 am), 
and whole day (12 am to 12 am). 
"""

"""
Percentage time in hyperglycemia (CGM > 180 mg/dL)
Percentage of time in hyperglycemia critical (CGM > 250 mg/dL)
Percentage time in range (CGM >= 70 mg/dL and CGM <= 180 mg/dL)
Percentage time in range secondary (CGM >= 70 mg/dL and CGM <= 150 mg/dL)
Percentage time in hypoglycemia level 1 (CGM < 70 mg/dL)
Percentage time in hypoglycemia level 2 (CGM < 54 mg/dL)
"""

"""
Case A: Manual mode
Case B: Auto mode
"""

