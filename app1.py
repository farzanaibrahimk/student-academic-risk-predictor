import streamlit as st
import pandas as pd
import joblib


st.set_page_config(page_title="Student Pass Predictor", page_icon="🎓", layout="centered")


# Load Model and Scaler using joblib with caching

def load_assets():
    model = joblib.load("streamlit_model.pkl")
    scaler = joblib.load("Scaler.pkl")
    return model, scaler

model, scaler = load_assets()


# App Header
st.title("🎓 Student Exam Pass/Fail Predictor")
st.write("Enter the student's key performance metrics below to predict their exam outcome.")

st.image("student_banner.png", use_container_width=True)


st.divider()

# --- Input Form for the Top 5 Features ---
st.subheader("Student Metrics Input")

prev_score = st.slider("Previous Exam Score", 0.0, 100.0, 65.0)
practice_tests = st.slider("Practice Tests Completed", 0, 20, 3)
prep_days = st.slider("Exam Preparation Days", 0, 60, 14)
study_hours = st.slider("Study Hours per Day", 0.0, 15.0, 4.0)
attendance = st.slider("Attendance Percentage (%)", 0.0, 100.0, 75.0)

# Prediction Button
if st.button("Predict Pass Status", type="primary"):
    # 1. Create DataFrame with the exact column names and order your model expects
    input_data = pd.DataFrame(
        [[prev_score, practice_tests, prep_days, study_hours, attendance]],
        columns=[
            'previous_exam_score',
            'practice_tests_completed',
            'exam_preparation_days',
            'study_hours_per_day',
            'attendance_percentage'
        ]
    )

    try:
        # 2. Scale the input data
        input_scaled = scaler.transform(input_data)

        # 3. Predict pass status and probabilities
        prediction = model.predict(input_scaled)[0]

        st.divider()
        st.subheader("Prediction Results")

        # 4. Display output visually
        if prediction == 1:
            st.success(f"🎉PASS")
            st.balloons()
        else:
            st.error(f"⚠️ FAIL")
            st.info("💡 **Recommendation:** Additional tutoring and extra practice tests advised.")

    except Exception as e:
        st.error(f"⚠️ An error occurred during prediction: {e}")