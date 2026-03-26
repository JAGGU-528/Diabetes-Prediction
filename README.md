# 🩺 Diabetes Prediction — ML Model Deployment

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Online-brightgreen?style=for-the-badge&logo=render)](https://diabetes-prediction-pimu.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.1.2-black?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.7.2-orange?style=for-the-badge&logo=scikit-learn)](https://scikit-learn.org)
[![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?style=for-the-badge&logo=render)](https://render.com)

> **A complete end-to-end Machine Learning web application** — from training a model in Jupyter Notebook to deploying it live on the internet for anyone to use.

---

## 🌍 Live Application

**Try it now:** [https://diabetes-prediction-pimu.onrender.com](https://diabetes-prediction-pimu.onrender.com)

> ⚠️ **Note:** The app uses a free hosting tier — it may take **30-50 seconds** to wake up on first visit. Please be patient!

---

## 📸 Preview

| Input Form | Prediction Result |
|---|---|
| Fill in 8 patient details | Instant prediction with color coding |
| Input validation included | ✅ No Diabetes (Green) / ⚠️ Has Diabetes (Red) |

---

## 📌 Project Overview

This project demonstrates the **complete ML deployment pipeline** — not just model training, but taking a trained model all the way to a live, accessible web application.

| Phase | Topic | Status |
|---|---|---|
| Phase 1 | Save & Load Model (joblib) | ✅ Complete |
| Phase 2 | Flask REST API | ✅ Complete |
| Phase 3 | HTML Frontend | ✅ Complete |
| Phase 4 | Connect UI to API | ✅ Complete |
| Phase 5 | Cloud Deployment (Render) | ✅ Live! |
| Phase 6 | Capstone | ✅ Complete |

---

## 🧠 Model Details

- **Dataset:** Pima Indians Diabetes Dataset (768 samples, 8 features)
- **Algorithm:** Decision Tree Classifier (tuned with GridSearchCV)
- **Key Metric:** Recall — because missing a diabetic patient is more dangerous than a false alarm
- **Pipeline:** SimpleImputer (median) → DecisionTreeClassifier
- **Best Depth:** 7 (found via GridSearchCV with `scoring='recall'`)
- **Test Recall:** 0.76 (catches 76% of actual diabetic patients)
- **Test Accuracy:** 73%

### Why Decision Tree over Logistic Regression?

| Model | CV Accuracy | Recall (Diabetic) |
|---|---|---|
| Logistic Regression | 0.77 | 0.62 |
| Naive Bayes | 0.75 | 0.69 |
| **Decision Tree (Tuned)** | **0.72** | **0.76** ✅ |

> In a medical context, **False Negatives are dangerous** — telling a diabetic patient they are healthy. Decision Tree minimizes this risk with the highest Recall score.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python 3 | Core language |
| Scikit-Learn | ML model training and pipeline |
| joblib | Model serialization (.pkl) |
| Flask | REST API backend |
| HTML + CSS | Frontend interface |
| JavaScript (fetch) | Connects frontend to API |
| GitHub | Version control |
| Render | Cloud hosting (free tier) |
| gunicorn | Production WSGI server |

---

## 📁 Project Structure

```
Diabetes-Prediction/
├── app.py                      ← Flask application (API + routes)
├── diabetes_model.pkl          ← Trained ML pipeline (saved with joblib)
├── requirements.txt            ← Python dependencies
├── diabetes.csv                ← Dataset (Pima Indians Diabetes)
├── templates/
│   └── index.html              ← Frontend (HTML + CSS + JavaScript)
├── DIABETES PREDICTION — CAPSTONE PROJECT.ipynb   ← Model training notebook
└── Model Deployment.ipynb      ← Deployment steps notebook
```

---

## ⚙️ How It Works

```
User fills form on browser
        ↓
JavaScript validates input (empty fields + medical ranges)
        ↓
fetch() sends POST request to Flask /predict
        ↓
Flask validates fields → creates pandas DataFrame
        ↓
joblib loads diabetes_model.pkl
        ↓
Pipeline: SimpleImputer → DecisionTreeClassifier
        ↓
Flask returns JSON {"prediction": "Has Diabetes"}
        ↓
JavaScript displays result (Red/Green color coded)
```

---

## 🚀 Run Locally

### Prerequisites
- Python 3.x
- pip

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/JAGGU-528/Diabetes-Prediction.git
cd Diabetes-Prediction

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Flask app
python app.py

# 4. Open in browser
# Go to: http://localhost:5000
```

---

## 🔒 Input Validation

The app includes **two layers of validation:**

**Frontend (JavaScript):**
- All 8 fields must be filled
- Medical range checks (e.g., Age: 1-120, BMI: 10-70)

**Backend (Flask):**
- Missing field detection
- Returns HTTP 400 with error message if fields are missing

| Field | Valid Range |
|---|---|
| Pregnancies | 0 – 20 |
| Glucose | 50 – 250 |
| Blood Pressure | 30 – 150 |
| Skin Thickness | 0 – 100 |
| Insulin | 0 – 900 |
| BMI | 10 – 70 |
| Diabetes Pedigree Function | 0.05 – 2.5 |
| Age | 1 – 120 |

---

## 📊 Dataset

- **Name:** Pima Indians Diabetes Dataset
- **Source:** Originally from National Institute of Diabetes and Digestive and Kidney Diseases
- **Rows:** 768 patients
- **Features:** 8 medical measurements
- **Target:** Outcome (0 = No Diabetes, 1 = Has Diabetes)
- **Class Distribution:** 65.1% No Diabetes / 34.9% Has Diabetes

---

## 🐛 Real Deployment Bugs Fixed

| Bug | Cause | Fix Applied |
|---|---|---|
| `gunicorn: command not found` | Missing from requirements.txt | Added `gunicorn` |
| `sklearn version mismatch` | Render installed newer version | Pinned `scikit-learn==1.7.2` |
| `No open HTTP ports` | Wrong PORT config | Fixed `os.environ.get('PORT')` |
| Silent wrong predictions | Empty fields as NaN | Added JS + Flask validation |
| Out-of-range values accepted | No input limits | Added min/max range validation |

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Jagdish Biradar**

[![GitHub](https://img.shields.io/badge/GitHub-JAGGU--528-181717?style=flat&logo=github)](https://github.com/JAGGU-528)

---

## 🙏 Acknowledgements

- Dataset: Pima Indians Diabetes Database
- Mentor & Guide: [Claude.ai by Anthropic](https://claude.ai)
- Hosting: [Render](https://render.com)

---

> *"You built the engine in Scikit-Learn. Then you put it in a car and drove it on the internet."*
> — Claude.ai
