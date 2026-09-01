Smart Student Predictor 🎓🤖

A Machine Learning project that predicts a student’s expected final score based on study-related features.

📌 Overview

Smart Student Predictor is an educational Machine Learning project built with Python and Scikit-learn.

The model uses the following features:

* 📚 Study Hours
* 📅 Attendance
* 📝 Previous Score
* 😴 Sleep Hours

It then predicts the student’s expected Final Score.

Note: This project is for educational and demonstration purposes only. It should not be used to make real decisions about students.

🧠 Machine Learning Workflow

Student Data
     ↓
Data Cleaning
     ↓
Feature Selection
     ↓
Train / Test Split
     ↓
Linear Regression
     ↓
Model Evaluation
     ↓
Save Model
     ↓
Make Predictions

🛠️ Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Matplotlib
* Google Colab
* Git & GitHub

📂 Project Structure

Smart-Student-Predictor/
│
├── data/
│   └── students.csv
│
├── models/
│   └── student_model.pkl
│
├── notebooks/
│   └── analysis.ipynb
│
├── src/
│   ├── preprocess.py
│   ├── train.py
│   └── predict.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore

⚙️ Installation

Clone the repository:

git clone https://github.com/Yassir050/Smart-Student-Predictor.git
cd Smart-Student-Predictor

Install the dependencies:

pip install -r requirements.txt

🚀 Training the Model

Run:

python src/train.py

The program will:

1. Load the dataset.
2. Clean the data.
3. Split the data into training and testing sets.
4. Train a Linear Regression model.
5. Calculate MAE and R².
6. Save the trained model.

🔮 Making a Prediction

Run:

python src/predict.py

Example input:

Study Hours: 6
Attendance: 92
Previous Score: 75
Sleep Hours: 7

The model returns a predicted final score.

📊 Model Evaluation

The project evaluates the model using:

* MAE (Mean Absolute Error) — measures the average prediction error.
* R² Score — measures how well the model explains the variation in the target values.

The exact results depend on the dataset and train/test split.

🎯 Skills Demonstrated

This project demonstrates practical skills in:

* Data preprocessing
* Exploratory data analysis
* Feature selection
* Regression
* Train/Test splitting
* Model evaluation
* Model persistence
* Making predictions with a trained model
* Python project organization

👨‍💻 Author

Yassir.B

Built as part of my journey toward becoming an AI Engineer.

📄 License

This project is intended for educational and portfolio purposes.
