import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("trained_model.pkl", "rb"))

st.title("Disease Prediction System")
st.write("Enter patient details:")

age = st.number_input("Age", 1, 100)

gender = st.selectbox("Gender", ["Male", "Female"])
bp = st.selectbox("Blood Pressure", ["Low", "Normal", "High"])
chol = st.selectbox("Cholesterol", ["Low", "Normal", "High"])

glucose = st.selectbox("Glucose", ["Normal", "High"])

smoking = st.selectbox("Smoking", ["No", "Yes"])
alcohol = st.selectbox("Alcohol Consumption", ["No", "Yes"])
exercise = st.selectbox("Exercise", ["No", "Yes"])

bmi = st.number_input("BMI(Body Mass Index)", 10.0, 50.0)

# family = st.selectbox("Family History", ["No", "Yes"])


gender_map = {"Male": 1, "Female": 0}
bp_map = {"High": 0,"Low": 1, "Normal": 2}
chol_map = { "High": 0,"Low": 1, "Normal": 2}
glu_map = {"High":0,"Normal":1}
yes_no_map = {"No": 0, "Yes": 1}


if st.button("Predict"):

    input_data = np.array([[
        age,
        gender_map[gender],
        bp_map[bp],
        chol_map[chol],
        glu_map[glucose],
        yes_no_map[smoking],
        yes_no_map[alcohol],
        yes_no_map[exercise],
        bmi,
        yes_no_map["No"]
    ]])

    prediction = model.predict(input_data)

    diseases = [
        'Heart Disease','Diabetes','Stroke','Kidney Disease','Cancer'
    ]

    st.subheader("Prediction Result:")

    found = False
    for i, val in enumerate(prediction[0]):
        if val == 1:
            st.warning(f" {diseases[i]} Detected")
            found = True

    if not found:
        st.success("No Disease Detected")
