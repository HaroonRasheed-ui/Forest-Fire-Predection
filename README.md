
# Forest Fire Prediction Project

This project focuses on predicting forest fires using machine learning techniques, specifically a neural network regression model. The dataset used for this project is sourced from Kaggle.




## Authors

- [@Haroon Rasheed](https://github.com/HaroonRasheed-ui)


## Overview

The goal of this project is to develop a predictive model that can estimate the potential area of a forest fire based on various environmental features. The project uses a neural network regression model implemented with TensorFlow/Keras.
## Files and Directories

forestfires.csv: Dataset for forestfire taken from the Kaggle.
EDA.ipynb: Google_Colab notebook in which EDA is performed on the dataset.
Model_tarining.ipynb: In this the model is being training upon the the dataset.
preprocess.py: It's a python file in which the data was processed before the process started. 
train_model.py: Now the train model is saved in python file for future use.
predict.py: In this python file, the project predict the fire according the save train_model.
app.py: In this python file, the streamlit app is running in the back server providing the interface for prediction. 
README.md: This file, providing an overview of the project.
## Getting started

To run this project, follow these steps:

1. Set Up the Environment:

Make sure you have Python installed on your system.

2. Data Preparation:

Place the dataset forestfires.csv in the project directory.

3. Running the colab Notebook:
## Project Structure

The Jupyter Notebook forest_fire_prediction.ipynb contains the entire codebase organized into sections with comments.
The dataset forestfires.csv contains the necessary data for training and testing the model.
## Dependencies

The project uses the following Python libraries:

pandas
numpy
sklearn
tensorflow

You can find the complete list of dependencies in the requirements.txt file.
## Notes

This project is a basic implementation of a forest fire prediction model. Further improvements can be made by experimenting with different algorithms, feature engineering, and hyperparameter tuning.