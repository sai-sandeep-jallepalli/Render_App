import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "../data/dataset.csv")
MODEL_PATH = os.path.join(BASE_DIR, "../data/model.joblib")
LOG_FILE = os.path.join(BASE_DIR, "../data/app.log")