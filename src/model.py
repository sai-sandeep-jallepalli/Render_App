import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from config import DATA_PATH, MODEL_PATH
from utils import validate_dataset
from logger import log

def train_model():
    if not validate_dataset():
        log("Dataset validation failed. Training aborted.", "error")
        return
    
    df = pd.read_csv(DATA_PATH)
    X = df[["Study Hours"]]
    y = df["Grade"]
    
    model = LinearRegression()
    model.fit(X, y)
    
    joblib.dump(model, MODEL_PATH)
    log("Model trained and saved successfully.")

if __name__ == "__main__":
    train_model()