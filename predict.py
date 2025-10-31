import streamlit as st
import pickle
import pandas as pd

def main():
    st.title("Heart Attack Prediction App")

    # Load model
    with open("final_best_model.pkl", "rb") as f:
        model = pickle.load(f)

    st.subheader("Masukkan Data Pasien")

    # Input Form
    age = st.number_input("Age", min_value=0, step=1)
    restingbp = st.number_input("Resting Blood Pressure", min_value=0)
    cholesterol = st.number_input("Cholesterol", min_value=0)
    fastingbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
    maxhr = st.number_input("Max Heart Rate Achieved", min_value=0)
    oldpeak = st.number_input("Oldpeak", min_value=0.0, format="%.1f")

    sex = st.selectbox("Sex", ["M", "F"])
    chestpaintype = st.selectbox("Chest Pain Type", ["ATA", "NAP", "ASY", "TA"])
    restingecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
    exerciseangina = st.selectbox("Exercise Induced Angina", ["Y", "N"])
    st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

    # Build Input
    input_dict = {
        "age": age,
        "restingbp": restingbp,
        "cholesterol": cholesterol,
        "fastingbs": fastingbs,
        "maxhr": maxhr,
        "oldpeak": oldpeak,
        "sex": sex,
        "chestpaintype": chestpaintype,
        "restingecg": restingecg,
        "exerciseangina": exerciseangina,
        "st_slope": st_slope
    }

    input_df = pd.DataFrame([input_dict])

    # Prediction
    if st.button("Predict"):
        try:
            prediction = model.predict(input_df)
            st.success(f"Prediction: {'Heart Disease' if prediction[0] == 1 else 'No Heart Disease'}")
        except Exception as e:
            st.error(f"Prediction failed: {e}")

if __name__ == "__main__":
    main()
