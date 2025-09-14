# 🎧 Podcast Listening Time Predictor  

This project was developed as part of a **Kaggle Competition**.  
The goal is to predict how long users are likely to listen to a podcast episode based on various features such as genre, episode length, host popularity, guest popularity, publication day/time, ads, and sentiment.  

---

## 🚀 Project Overview  
- **Type:** Regression Problem  
- **Competition Platform:** Kaggle  
- **Objective:** Predict podcast listening time (in minutes).  
- **Approach:**  
  - Preprocessing with Label Encoding, OneHot Encoding, and Standard Scaling.  
  - Model trained using **XGBoost Regressor**.  
  - Deployment via **Streamlit** for interactive UI.  

---

## 🛠️ Tech Stack  
- **Python** 🐍  
- **Libraries:** `pandas`, `numpy`, `scikit-learn`, `xgboost`, `pickle`, `streamlit`  
- **Deployment:** Streamlit app  

---

## 📂 Repository Structure  
📦 Podcast-Listening-Time-Predictor
├── 📁 notebooks/ # Kaggle notebooks & EDA
├── 📁 models/ # Saved pickle models
│ ├── label_encoder.pkl
│ ├── onehot_encoder.pkl
│ ├── scaler.pkl
│ └── xgb_model.pkl
├── app.py # Streamlit App
├── requirements.txt # Dependencies
└── README.md # Project Documentation
