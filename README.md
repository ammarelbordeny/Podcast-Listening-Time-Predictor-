# 🎧 Podcast Listening Time Predictor  
This project was developed as part of a **Kaggle Competition**.  
The goal is to predict how long users are likely to listen to a podcast episode based on various features such as genre, episode length, host popularity, guest popularity, publication day/time, ads, and sentiment.  

![Streamlit App Screenshot](https://github.com/ammarelbordeny/Podcast-Listening-Time-Predictor-/blob/main/images/Screenshot%202025-09-15%20015054.png)
*Interactive Streamlit application for podcast listening time prediction*

---
## 🚀 Project Overview  
- **Type:** Regression Problem  
- **Competition Platform:** Kaggle  
- **Evaluation Metric:** Root Mean Square Error (RMSE)
- **Achieved Score:** **12.869090** 🏆
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
```text
📦 Podcast-Listening-Time-Predictor
├── 📁 notebooks/              # Training model notebook
├── 📁 models/                 # Saved pickle models
│   ├── label_encoder.pkl
│   ├── onehot_encoder.pkl
│   ├── scaler.pkl
│   └── xgb_model.pkl
├── 📁 images/                 # Screenshots and images
│   └── streamlit_app_screenshot.png
├── app.py                     # Streamlit App
├── requirements.txt           # Dependencies
└── README.md                  # Project Documentation
```

---
## 🔧 Installation & Setup

### Prerequisites
Make sure you have Python 3.7+ installed on your system.

### 1. Clone the Repository
```bash
git clone https://github.com/ammarelbordeny/Podcast-Listening-Time-Predictor.git
cd Podcast-Listening-Time-Predictor
```

### 2. Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv podcast_env

# Activate virtual environment
# On Windows:
podcast_env\Scripts\activate
# On macOS/Linux:
source podcast_env/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---
## 🏃‍♂️ Running the Application

### Run Streamlit App
```bash
streamlit run app.py
```

The app will automatically open in your default web browser at `http://localhost:8501`

### Alternative: Run with Custom Port
```bash
streamlit run app.py --server.port 8502
```

---
## 🎯 How to Use the App

1. **Launch the Application:** Run the Streamlit command above
2. **Input Features:** Enter the podcast episode details in the sidebar:
   - Genre selection
   - Episode length (minutes)
   - Host popularity score
   - Guest popularity score
   - Publication day and time
   - Number of ads
   - Sentiment analysis score
3. **Get Prediction:** Click the "Predict Listening Time" button
4. **View Results:** The predicted listening time will be displayed instantly

---
## 🧠 Model Performance
- **Algorithm:** XGBoost Regressor
- **Preprocessing:** Label Encoding, OneHot Encoding, Standard Scaling
- **Features:** Genre, episode length, host popularity, guest popularity, publication timing, ads, sentiment

---
## 📊 Features Used for Prediction
- **Genre:** Podcast category (Comedy, News, Technology, etc.)
- **Episode Length:** Duration of the podcast episode
- **Host Popularity:** Popularity score of the podcast host
- **Guest Popularity:** Popularity score of the guest (if any)
- **Publication Day:** Day of the week the episode was published
- **Publication Time:** Time of day the episode was published
- **Number of Ads:** Count of advertisements in the episode
- **Sentiment Score:** Sentiment analysis score of the episode content

---
## 🤝 Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---
## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
## 🙏 Acknowledgments
- Kaggle for hosting the competition
- XGBoost developers for the excellent gradient boosting framework
- Streamlit team for the amazing web app framework
