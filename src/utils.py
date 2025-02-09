import pandas as pd
import os
from config import DATA_PATH
from logger import log

def validate_dataset():
    if not os.path.exists(DATA_PATH):
        log("Dataset not found!", "error")
        return False
    
    df = pd.read_csv(DATA_PATH)
    
    expected_columns = ["Study Hours", "Grade"]
    if list(df.columns) != expected_columns:
        log("Incorrect column names!", "error")
        return False
    
    if df.isnull().sum().sum() > 0:
        log("Dataset contains missing values!", "error")
        return False
    
    log("Dataset validated successfully.")
    return True
