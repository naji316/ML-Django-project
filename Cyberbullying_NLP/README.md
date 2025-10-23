 
# 🧠 Cyberbullying Detection (NLP + Django)

This project detects cyberbullying using Natural Language Processing (NLP) and a Machine Learning model integrated with Django.

## 🚀 Features
- Real-time text classification (cyberbullying or not)
- Django frontend + REST API
- TF-IDF + ML model (e.g., Logistic Regression / SVM)
- Easy to extend for more labels (religion, gender, age, etc.)

## 🧩 Tech Stack
- Python (scikit-learn, numpy, pandas)
- Django Framework
- HTML, CSS, JavaScript (frontend)
- Pickle model for ML integration

## 🧠 How It Works
1. User inputs text.
2. Text is vectorized using TF-IDF.
3. Model predicts if it's cyberbullying or not.
4. Result shown instantly in the Django web app.

## 🧰 Setup Instructions
```bash
git clone https://github.com/naji316/ML-Django-project.git
cd ML-Django-project/cyberbulling-NLP
pip install -r requirements.txt
python manage.py runserver




Then open http://127.0.0.1:8000/ in your browser.





📁 Folder Structure
cyberbulling-NLP/
├── manage.py
├── Cyberbullying_NLP/
├── static/
├── templates/
├── ml_model.pkl
├── vectorizer.pkl
└── README.md


👤 Author

Naji — Django & AI Developer