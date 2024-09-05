import tensorflow as tf
from preprocess import preprocess_data
import pandas as pd

def train_and_save_model():
    # Load and preprocess the data
    data = pd.read_csv('forestfires.csv')
    X, y = preprocess_data(data)
    
    # Build the model
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(X.shape[1],)),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(1)
    ])
    
    # Compile the model
    model.compile(optimizer='adam', loss='mse')
    
    # Train the model
    model.fit(X, y, epochs=500, verbose=1)
    
    # Save the model using the Keras format
    model.save('models/forest_fire_model.keras')

if __name__ == "__main__":
    train_and_save_model()
