import tensorflow as tf
import numpy as np
import pandas as pd
from preprocess import preprocess_data
from tensorflow.keras.losses import MeanSquaredError
from tensorflow.keras.saving import register_keras_serializable

@register_keras_serializable()
def mse(y_true, y_pred):
    return MeanSquaredError()(y_true, y_pred)

def load_model():
    # Load the model and ensure the custom 'mse' function is recognized
    return tf.keras.models.load_model('models/forest_fire_model.h5', custom_objects={'mse': mse})

def make_prediction(input_data):
    model = load_model()
    data = pd.DataFrame([input_data])
    X, _ = preprocess_data(data)  # Preprocess the input data
    prediction = model.predict(X)  # Make the prediction
    return np.expm1(prediction[0][0])  # Convert the prediction from log scale

if __name__ == "__main__":
    # Define the input data for prediction
    input_data = {
        'X': 7,
        'Y': 5,
        'month': 'mar',
        'day': 'fri',
        'FFMC': 86.2,
        'DMC': 26.2,
        'DC': 94.3,
        'ISI': 5.1,
        'temp': 8.2,
        'RH': 51,
        'wind': 6.7,
        'rain': 0.0
    }
    # Make the prediction and print the result
    prediction = make_prediction(input_data)
    print(f'Predicted burned area: {prediction:.2f} ha')
