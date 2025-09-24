# 🌾 Crop Prediction System

A machine learning–powered web application that predicts the most suitable crop for cultivation based on soil and climate conditions.

## 🚀 Project Overview

The goal of this project is to help farmers make informed decisions about which crop to cultivate by analyzing soil nutrients, pH, temperature, humidity, and rainfall.

* Uses **Random Forest Classifier** for accurate crop prediction (99% accuracy achieved on dataset).
* Accepts inputs such as **N, P, K values, pH, temperature, humidity, and rainfall**.
* Predicts the best crop from **21 possible crops**.
* Built with **Flask** for backend and **HTML, CSS, JavaScript** for frontend.
* Deployed on **Render** for easy accessibility.

👉 Live Demo: [Crop Prediction App](https://crop-prediction-1-aaao.onrender.com/)

---

## 🧑‍🌾 Features

* ✅ User-friendly web interface for inputting soil and climate data
* ✅ Machine learning model trained on historical crop and climate dataset
* ✅ Real-time crop recommendation with high accuracy
* ✅ Extendable for future features like **market price prediction** and **yield estimation**

---

## 🛠️ Tech Stack

* **Python** (pandas, scikit-learn, joblib)
* **Flask** (backend framework)
* **HTML, CSS, JavaScript** (frontend UI)
* **Render** (deployment)

---

## 📂 Project Structure

```
├── app.py               # Flask backend
├── templates/           # HTML templates
├── static/              # CSS, JS, assets
├── model/               # Trained ML model (saved using joblib)
├── data/                # Dataset (CSV)
└── README.md            # Project documentation
```

---

## ▶️ How to Run Locally

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/crop-prediction.git
   cd crop-prediction
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   python app.py
   ```

4. Open in browser:

   ```
   http://127.0.0.1:5000/
   ```

---

## 📊 Model Performance

* **Algorithm:** Random Forest Classifier
* **Accuracy:** \~99% (validated on dataset)
* **Classes:** 21 crop types
