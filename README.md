# Heart-attack-prediction


## Heart Attack Prediction App

This project is a Machine Learning web application built using Streamlit to predict the likelihood of a heart attack based on several health parameters.
The model was trained using various classification algorithms such as K-Nearest Neighbors (KNN), Support Vector Machine (SVM), Decision Tree, Random Forest, and Gradient Boosting, with KNN selected as the best-performing model after hyperparameter tuning.

## Features

- Interactive web interface for user input

- Pretrained machine learning model for heart attack prediction

- Automated data preprocessing using the same pipeline as the training phase

- Real-time predictions with clear output labels

Heart-Attack-Prediction/

├─ app.py                 # Streamlit web application

├─ final_best_model.pkl   # Saved trained model (KNN)

├─ requirements.txt       # Python dependencies

└─ README.md              # Project documentation


## Model Training Overview

- Dataset: Heart Failure Prediction Dataset (Kaggle)

- Goal: Predict whether a person is likely to have a heart attack

- Evaluation Metric: Recall

- Best Model: K-Nearest Neighbors (KNN)

- Test Accuracy: ~90%

The KNN model achieved the highest recall and test accuracy compared to other algorithms after hyperparameter tuning.


## Requirements

- Python 3.9+

- Streamlit

- Pandas

- Scikit-learn

- Pickle

All dependencies are listed in the requirements.txt file.

## Author

Developed by bUtekwijay as part of a machine learning project focusing on heart disease prediction.
