import streamlit as st
import pickle
import numpy as np
import pandas as pd
import time

# =========================
# Load saved files
# =========================
with open("label_encoder.pkl", "rb") as f:
    label_enc = pickle.load(f)

with open("onehot_encoder.pkl", "rb") as f:
    onehot = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("xgb_model.pkl", "rb") as f:
    model = pickle.load(f)

# =========================
# Streamlit UI
# =========================
st.set_page_config(page_title="Podcast Listening Time Predictor", page_icon="🎧", layout="centered")

# Title with animation
st.markdown(
    """
    <h1 style="text-align:center; color:#4CAF50; animation: fadeIn 2s;">
        🎧 Podcast Listening Time Predictor
    </h1>
    <style>
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("### Enter episode details to predict the expected listening time")

# User inputs
episode_length = st.slider("Episode Length (minutes)", 10.0, 200.0, 60.0)
genre = st.selectbox("Genre", onehot.categories_[0])   # from fitted encoder
host_pop = st.slider("Host Popularity (%)", 0.0, 100.0, 50.0)
pub_day = st.selectbox("Publication Day", onehot.categories_[1])  # from fitted encoder
pub_time = st.selectbox("Publication Time", onehot.categories_[2])  # from fitted encoder
guest_pop = st.slider("Guest Popularity (%)", 0.0, 100.0, 50.0)
ads = st.number_input("Number of Ads", min_value=0, max_value=10, value=2)
sentiment = st.selectbox("Episode Sentiment", label_enc.classes_)  # from fitted encoder

# =========================
# Data processing & Prediction
# =========================
if st.button("🔮 Predict Listening Time"):
    with st.spinner("✨ Analyzing your podcast details..."):
        time.sleep(1.5)  # animation delay

        try:
            # Create DataFrame
            input_df = pd.DataFrame({
                "Episode_Length_minutes": [episode_length],
                "Genre": [genre],
                "Host_Popularity_percentage": [host_pop],
                "Publication_Day": [pub_day],
                "Publication_Time": [pub_time],
                "Guest_Popularity_percentage": [guest_pop],
                "Number_of_Ads": [ads],
                "Episode_Sentiment": [sentiment]
            })

            # Label encoding
            input_df["Episode_Sentiment"] = label_enc.transform(input_df["Episode_Sentiment"])

            # OneHot encoding
            onehot_features = onehot.transform(input_df[["Genre", "Publication_Day", "Publication_Time"]]).toarray()
            onehot_df = pd.DataFrame(
                onehot_features,
                columns=onehot.get_feature_names_out(["Genre", "Publication_Day", "Publication_Time"])
            )

            # Combine
            input_df_final = pd.concat(
                [input_df.drop(["Genre", "Publication_Day", "Publication_Time"], axis=1).reset_index(drop=True),
                 onehot_df.reset_index(drop=True)],
                axis=1
            )

            # Scaling
            input_scaled = scaler.transform(input_df_final)

            # Prediction
            pred = model.predict(input_scaled)[0]

            # Fancy result box
            st.markdown(
                f"""
                <div style="padding:20px; border-radius:15px; background-color:#f0f8ff; text-align:center; box-shadow:2px 2px 12px #aaa;">
                    <h2 style="color:#2E8B57;">⏱️ Estimated Listening Time</h2>
                    <h1 style="color:#FF4500;">{pred:.2f} minutes</h1>
                </div>
                """,
                unsafe_allow_html=True
            )

        except Exception as e:
            st.error(f"⚠️ Error during prediction: {e}")
