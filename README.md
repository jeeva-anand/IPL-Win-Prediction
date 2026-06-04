# IPL Win Prediction

## Project Overview

IPL Win Probability Predictor is a machine learning application that predicts the winning probability of teams during live IPL matches. Using historical IPL data and match-specific features, the model provides real-time win probability estimates based on the current state of the game.

![alt text](assets/screenshots/image.png)

## Project Structure

```

ipl-win-predictor/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── raw/
│   │   ├── matches.csv
│   │   └── deliveries.csv
│   │
│   └── processed/
│       └── final_df.csv
│
├── notebooks/
│   └── experimentation.ipynb
│
├── src/
│   ├── __init__.py
│   ├── preprocess.py
│   ├── model_training.py
│   └── helper.py
│
├── models/
│   └── pipe.pkl
│
└── assets/
    └── screenshots/

```

## Key Features

### Exploratory Data Analysis (EDA)

* Analyzed historical IPL match data to identify trends and factors influencing match outcomes.
* Explored team performance, venue statistics, and match-winning patterns.
* Visualized distributions and relationships between key match variables.

### Data Preprocessing

* Cleaned and transformed raw IPL datasets.
* Handled missing values and irrelevant features.
* Prepared match-level data for machine learning modeling.

### Feature Engineering

* Created match-specific features such as:

  * Runs required
  * Balls remaining
  * Current run rate (CRR)
  * Required run rate (RRR)
  * Wickets remaining
  * Batting and bowling teams
  * Host venue

### Train-Test Split

* Split the dataset into training and testing sets to evaluate model generalization and prevent overfitting.

### Machine Learning Model Development

* Implemented and trained machine learning models to predict match outcomes.
* Evaluated model performance using appropriate classification metrics.
* Selected the best-performing model for deployment.

### Web Application Development

* Built an interactive Streamlit application for real-time IPL win probability prediction.
* Designed a user-friendly interface allowing users to input live match conditions and receive instant predictions.

### Deployment

* Deployed the application on Streamlit Community Cloud.
* Enabled public access for real-time prediction and demonstration.

## Technologies Used

Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Streamlit

## Outcomes

* Developed an end-to-end machine learning solution for sports analytics.
* Generated real-time win probability predictions for IPL matches.
* Demonstrated expertise in data preprocessing, feature engineering, machine learning, web application development, and deployment.

This format is professional, recruiter-friendly, and aligns well with GitHub portfolio standards. It focuses on the **problem, methodology, features, deployment, and outcome** rather than just listing notebook steps.

