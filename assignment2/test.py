#!/usr/bin/env python3

import pandas as pd
import pickle
from train import extract_features
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

with open("model.pkl", "rb") as model_file:
    trained_model = pickle.load(model_file)

"""omitted"""

pd.DataFrame(predictions).to_csv("Result.csv", header=False, index=False)
