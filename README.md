
# Student Academic Risk Prediction System

## Project Overview

The Student Academic Risk Prediction System is a machine learning-based web application developed to identify students who may be at academic risk based on their academic performance, preparation habits, and attendance.

The project aims to support early identification of students who may need additional academic guidance, helping educators take proactive steps rather than responding only after final examination results.

## Objectives

- Predict whether a student is likely to pass or be at academic risk.
- Identify important factors influencing academic performance.
- Provide an easy-to-use interface for entering student information and viewing predictions.
- Demonstrate the practical application of machine learning in educational analytics.

## Technologies Used

- Python
- Pandas and NumPy
- Scikit-learn
- Imbalanced-learn (SMOTE)
- Joblib
- Streamlit
- Matplotlib and Seaborn

## Input Features

The application uses the following five features:

1. Previous Exam Score
2. Practice Tests Completed
3. Exam Preparation Days
4. Study Hours Per Day
5. Attendance Percentage

## Project Workflow

1. Data loading and preprocessing
2. Exploratory Data Analysis (EDA)
3. Train-test splitting
4. Handling class imbalance using SMOTE on training data
5. Training and comparing multiple machine learning algorithms
6. Feature selection and hyperparameter tuning
7. Model evaluation
8. Saving the trained model and scaler using Joblib
9. Developing an interactive Streamlit application

## Machine Learning Model

Multiple classification algorithms were evaluated, including:

- Logistic Regression
- Decision Tree
- Random Forest
- Support Vector Machine
- K-Nearest Neighbors
- Naive Bayes

The final selected model was a tuned Logistic Regression classifier.

**Test Accuracy: 74%**

## Application Features

- Interactive input fields
- Student academic risk prediction
- Prediction confidence display
- Simple Streamlit interface

## Project Screenshots


### Pass status
!(screenshot 2-Pass_status.png)

### Prediction Result
!(screenshot 1-Failed_status.png)

## Installation and Execution

### 1. Clone the repository

```bash
git clone https://github.com/farzanaibrahimk/student-academic-risk-predictor.git
```

### 2. Navigate to the project folder

```bash
cd student-academic-risk-predictor
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

## Future Improvements

- Explore additional machine learning algorithms.
- Improve prediction performance through further feature engineering.
- Include more academic and behavioural indicators.
- Develop additional visualisations and insights.

## Disclaimer

This project is an educational machine learning prototype intended to support academic risk identification. Its predictions should not be treated as a definitive assessment of a student's academic ability.

