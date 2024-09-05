import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(data):
    # Expected training columns (12 features total)
    training_columns = [
        'X', 'Y', 'FFMC', 'DMC', 'DC', 'ISI', 'temp', 'RH', 'wind', 'rain',
        'month_aug', 'day_fri'
    ]

    # One-hot encode categorical features
    data = pd.get_dummies(data, columns=['month', 'day'], drop_first=True)

    # Add missing columns with zeros to match training columns
    for col in training_columns:
        if col not in data.columns:
            data[col] = 0

    # Select the columns used during training
    data = data[training_columns]

    # Scale the numerical features
    scaler = StandardScaler()
    numerical_features = ['X', 'Y', 'FFMC', 'DMC', 'DC', 'ISI', 'temp', 'RH', 'wind', 'rain']
    data[numerical_features] = scaler.fit_transform(data[numerical_features])

    X = data
    y = None  # No target variable during prediction

    return X, y
