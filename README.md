# Credit Score and Loan Prediction

Overview

>This project is a machine learning-based web application for predicting credit scores and loan eligibility. It uses a Random Forest Classifier to predict credit scores based on various financial inputs and calculates the maximum loan amount based on the predicted credit score. The web interface is built using Flask.

Features

>Credit Score Prediction: Uses a trained machine learning model to predict credit scores.

>Loan Amount Prediction: Determines the maximum loan amount a user can receive based on financial inputs.

>Interactive Web Interface: Users can enter financial details through a simple web form.

>Data Visualization: Uses Plotly to visualize credit scores based on occupation.

Technologies Used

Python

Pandas & NumPy (Data Processing)

Scikit-learn (Machine Learning Model)

Plotly (Data Visualization)

Flask (Web Framework)

Flask-Ngrok (To expose local Flask app over the internet)

Installation

Prerequisites

>Ensure you have Python installed on your system. Then, install the required dependencies using:

>pip install pandas numpy plotly scikit-learn flask flask-ngrok

Running the Project

>Download or clone the repository.

>Ensure the dataset (train.csv) is available in the project directory.

>Run the Python script:-

python script.py

>Open the generated Ngrok URL in your browser to access the web application.

Usage

1.Enter financial details in the form fields.

2.Click the Predict button.

3.View the predicted credit score and eligible loan amount.

# Screenshot of the Project:-

![Screenshot 2025-03-26 232144](https://github.com/user-attachments/assets/f43a38a5-e0d4-4f4b-ae93-166b353bbc8a)
![Screenshot 2025-03-26 232159](https://github.com/user-attachments/assets/ac3d4aa4-4cf8-4eab-b30f-dcb6db0bd85a)


# Code Explanation :-

Machine Learning Model

The dataset is loaded and preprocessed.

Features like Annual Income, Credit Mix, and Outstanding Debt are used for training.

A Random Forest Classifier is trained to predict the credit score.

The trained model is used to predict loan eligibility.

# Web Application :

Flask is used to create a simple web interface.

A form collects user input and sends it to the model for prediction.

Predictions are displayed on a results page.
