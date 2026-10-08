from pathlib import Path
import pickle
import math

import pandas as pd
from flask import Flask, render_template, request

BASE_DIR = Path(__file__).resolve().parent
with (BASE_DIR / "rain_XGBnew_model.pkl").open("rb") as model_file:
    model = pickle.load(model_file)
app = Flask(__name__, template_folder="template", static_folder="Static")

# Preserve the numeric encodings supplied by the existing HTML form.
FEATURE_FIELDS = (
    "location", "mintemp", "maxtemp", "rainfall", "evaporation", "sunshine",
    "windgustdir", "windgustspeed", "winddir9am", "winddir3pm",
    "windspeed9am", "windspeed3pm", "humidity9am", "humidity3pm",
    "pressure9am", "pressure3pm", "cloud9am", "cloud3pm", "temp9am",
    "temp3pm", "raintoday",
)

@app.get("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "GET":
        return render_template("index.html")
    try:
        date = pd.to_datetime(request.form["date"], format="%Y-%m-%d", errors="raise")
        if pd.isna(date):
            raise ValueError("Date is required")
        features = [float(request.form[field]) for field in FEATURE_FIELDS]
        if not all(math.isfinite(value) for value in features):
            raise ValueError("Features must be finite")
        features.extend([float(date.month), float(date.day)])
    except (KeyError, TypeError, ValueError):
        return "Provide a valid date and numeric values for all weather fields.", 400
    output = model.predict([features])[0]
    return render_template("after_sunny.html" if output == 0 else "after_rainy.html")

if __name__ == "__main__":
    app.run(debug=True)
