from flask import Flask, request, render_template
import joblib
import numpy as np
from config import MODEL_PATH
from logger import log

app = Flask(__name__)

# Load Model
try:
    model = joblib.load(MODEL_PATH)
except:
    log("Model not found! Train the model first.", "error")
    model = None

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    if request.method == "POST":
        try:
            study_hours = float(request.form["study_hours"])
            prediction = model.predict(np.array(study_hours).reshape(-1, 1))[0]
        except Exception as e:
            log(f"Prediction error: {e}", "error")
            prediction = "Invalid input"
    
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
