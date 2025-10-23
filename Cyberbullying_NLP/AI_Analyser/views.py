from django.shortcuts import render
from django.conf import settings
from .forms import AnalysisForm
import os
import joblib
import pandas as pd

# --- Load models ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, 'ml_models')

try:
    logistic_model = joblib.load(os.path.join(MODEL_DIR, 'logistic_model.pkl'))
    tfidf = joblib.load(os.path.join(MODEL_DIR, 'tfidf_vectorizer.pkl'))
    label_encoder = joblib.load(os.path.join(MODEL_DIR, 'label_encoder.pkl'))
except FileNotFoundError as e:
    print(f"Error: {e}")
    raise


# --- Main view ---
def home(request):
    if request.method == "POST":
        form = AnalysisForm(request.POST, request.FILES)
        if form.is_valid():
            text = form.cleaned_data.get("input_text")
            file = request.FILES.get('file')
            results = []

            if file:  # Handle CSV upload
                try:
                    df = pd.read_csv(file)
                    if 'text' not in df.columns:
                        return render(request, "result.html", {
                            "error": "CSV must contain a column named 'text'."
                        })
                    # Transform text and predict
                    X = tfidf.transform(df['text'])
                    preds = logistic_model.predict(X)
                    decoded_preds = label_encoder.inverse_transform(preds)
                    df["prediction"] = decoded_preds
                    results = list(zip(df["text"], df["prediction"]))
                except Exception as e:
                    return render(request, "result.html", {'error': f"Error: {e}"})

            elif text:  # Handle single text input
                try:
                    text_vector = tfidf.transform([text])
                    pred = logistic_model.predict(text_vector)[0]
                    label = label_encoder.inverse_transform([pred])[0]
                    results = [(text, label)]
                except Exception as e:
                    results = [(text, f"Error during prediction: {e}")]

            return render(request, "result.html", {'results': results})

    else:
        form = AnalysisForm()

    return render(request, "home.html", {'form': form})
