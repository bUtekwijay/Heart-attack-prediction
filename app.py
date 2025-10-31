import streamlit as st
from eda import main as eda_main
from predict import main as predict_main

def main():
    # Sidebar Navigation
    st.sidebar.title("Heart Disease Prediction App")
    options = st.sidebar.radio("Navigate to:", ["EDA", "Prediction"])

    # Routing
    if options == "EDA":
        eda_main()  # Run the EDA module
    elif options == "Prediction":
        predict_main()  # Run the Prediction module

if __name__ == "__main__":
    main()