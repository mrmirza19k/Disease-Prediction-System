# 🩺 Disease Prediction System

## 📌 Overview

This project is a **Machine Learning-based Disease Prediction System** that predicts multiple diseases based on user health inputs.
It uses a trained **Random Forest Classifier** and a **Streamlit web interface** for real-time predictions.

---

## 🚀 Features

* Predicts multiple diseases:

  * Heart Disease
  * Diabetes
  * Stroke
  * Kidney Disease
  * Cancer
* User-friendly web interface using Streamlit
* Real-time prediction based on input parameters
* Multi-label classification model
* Rule-based label generation (for training dataset)

---

## 🧠 Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit
* Pickle (Model saving)

---

## 📊 Input Parameters

The model takes the following inputs:

* Age
* Gender
* Blood Pressure
* Cholesterol
* Glucose
* Smoking
* Alcohol Consumption
* Exercise
* BMI (Body Mass Index)
* Family History

---

## ⚙️ How It Works

1. Dataset is preprocessed and encoded
2. Rule-based logic is used to generate disease labels
3. A Random Forest model is trained on the dataset
4. The trained model is saved as `.pkl` file
5. Streamlit UI takes user input and predicts diseases

---

## ▶️ How to Run Locally

### Step 1: Clone Repository

```bash
git clone https://github.com/your-username/disease-prediction-app.git
cd disease-prediction-app
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run Application

```bash
streamlit run app.py
```

---

## 🌐 Live Demo

(Add your deployed link here after deployment)

---

## ⚠️ Limitations

* Dataset is synthetic (rule-based generated labels)
* Not suitable for real medical diagnosis
* Accuracy may vary with real-world data

---

## 🎯 Future Improvements

* Use real medical datasets
* Add risk percentage prediction
* Improve UI/UX
* Integrate with healthcare APIs

---

## 📌 Author

**Tabrej Ansari**
 AI Engineer & Data Analyst   

---

## 📜 License

This project is for educational purposes only.
