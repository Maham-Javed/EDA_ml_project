# EduCast: Student Performance Prediction Engine

## Overview
EduCast is an end-to-end **Exploratory Data Analysis (EDA) and Machine Learning project** designed to analyze and predict student academic performance. The project leverages statistical analysis, feature engineering, and multiple regression models to uncover patterns and build accurate predictive systems.

This project demonstrates a complete **machine learning pipeline**, from raw data exploration to deployment using Flask.

---

## Problem Statement
Student performance is influenced by multiple factors such as demographics, study habits, and socio-economic conditions.

The objective of this project is to:
- Perform in-depth **Exploratory Data Analysis (EDA)**
- Identify key factors affecting student performance
- Build and compare multiple **regression models**
- Predict student scores accurately
- Provide insights to improve academic outcomes

---

## Key Features
- Comprehensive EDA
- Data Cleaning & Preprocessing
- Feature Engineering
- Multiple Machine Learning Models
- Hyperparameter Tuning
- Model Performance Evaluation
- Flask Web Application for Predictions

---

## Project Structure

```
EDA_ml_project/
│
├── data/                  # Dataset files
├── notebooks/             # Jupyter notebooks (EDA & experimentation)
├── src/                   # Source code
│   ├── components/        # Data ingestion, transformation, training
│   ├── pipelines/         # Training & prediction pipelines
│   ├── utils/             # Helper utilities
│
├── templates/             # HTML templates for Flask
├── static/                # CSS/JS assets
├── app.py                 # Flask application
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
```

---

## Exploratory Data Analysis (EDA)

EDA was performed to understand the dataset and extract meaningful insights.

### Steps:
- Dataset overview and structure analysis
- Handling missing values
- Univariate analysis
- Bivariate analysis
- Correlation heatmaps
- Data visualization using Matplotlib & Seaborn

### Key Insights:
- Study habits significantly impact performance
- Parental education influences student outcomes
- Strong correlation observed between subject scores

---

## Data Preprocessing

- Handling missing/null values
- Encoding categorical variables
- Feature scaling (if applicable)
- Splitting dataset into training and testing sets

---

## Feature Engineering

- Transformation of categorical features
- Creation of meaningful derived variables
- Selection of important features for modeling

---

## Machine Learning Models

The following regression models were implemented:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- AdaBoost Regressor
- XGBRegressor (XGBoost)
- CatBoost Regressor

---

## Hyperparameter Tuning

Hyperparameter tuning was applied to improve model performance using techniques such as:
- Grid Search
- Random Search

---

## Model Evaluation

Models were evaluated using:

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)

The best-performing model was selected based on these evaluation metrics.

---

## Deployment (Flask App)

A Flask-based web application was developed to make predictions.

### How to Run Locally:

```bash
# Clone the repository
git clone https://github.com/Maham-Javed/EDA_ml_project.git

# Navigate to the project directory
cd EDA_ml_project

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
```

Then open your browser and go to:
```
http://127.0.0.1:5000/
```

---

## Tech Stack

**Language:** Python

**Libraries & Tools:**
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- CatBoost
- Flask

---

## Results & Insights

- Ensemble models outperformed linear models
- Feature engineering improved prediction accuracy
- Data visualization helped identify key influencing factors

---

## Future Improvements

- Deploy on cloud platforms (AWS, Render, etc.)
- Improve UI/UX of Flask application
- Add interactive dashboards
- Integrate database for data storage
- Experiment with deep learning models

---

## Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request.

---


