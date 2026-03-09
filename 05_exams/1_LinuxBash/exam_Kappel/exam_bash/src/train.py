"""
-------------------------------------------------------------------------------
This script runs the training of an XGBoost model to predict graphics card sales 
from the preprocessed data.

1. It starts by searching for the latest preprocessed CSV file in the 'data/processed/' directory.
2. If a standard model (model.pkl) does not exist, it loads the data, splits it into training and test sets, trains a model on this data, evaluates it, and then saves it as 'model/model.pkl'.
3. If a standard model already exists, it trains a new model on the latest data, evaluates it, and saves the model in the 'model/' folder in the format: model_YYYYMMDD_HHMM.pkl.
4. Performance metrics (RMSE, MAE, R²) are displayed and saved in the log file.
5. Any errors are handled and reported in the logs.

The models are saved in the 'model/' folder with the name 'model.pkl' for the standard model and with a timestamp for later versions.
The model metrics are recorded in the script’s log files.
-------------------------------------------------------------------------------
"""


import os
import pandas as pd
from xgboost import XGBRegressor
import joblib                   # store trained models
from datetime import datetime
import pickle

# Folder dir section
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # one level up

RAW_DIR = os.path.join(ROOT_DIR, "data", "processed")
MODEL_DIR = os.path.join(ROOT_DIR, "model")
LOG_FILE = os.path.join(ROOT_DIR, "logs", "train.logs")

def train_model():


    # logging and Foldercheck
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a") as log: 
        log.write(f"{datetime.now()} - Starting training\n")
    

    # latest csv
    files = [f for f in os.listdir(RAW_DIR) if f.endswith(".csv")]    # f.end not forgett
    if not files:
        raise FileNotFoundError("Np csv in Processing folder")
    #latest csv - Filename Date
    latest = max(files, key=lambda f: os.path.getmtime(os.path.join(RAW_DIR, f)))
    df = pd.read_csv(os.path.join(RAW_DIR, latest))



    # Feature eng

    if "model" not in df.columns or "sales" not in df.columns:
        raise ValueError("Expected columns 'model' and 'sales' not found.")
    #  
    X = pd.get_dummies(df["model"])   # One-hot encoding
    y = df["sales"]

    # # Model training
    # model = XGBRegressor()
    # model.fit(X, y)




    # # saving
    # os.makedirs(MODEL_DIR, exist_ok=True)        # NOT mkdir
    # model_path = os.path.join(MODEL_DIR, "model.pkl")

    # with open(model_path, "wb") as f:
    #     pickle.dump(model, f)

    # with open(LOG_FILE, "a") as log:
    #     log.write(f"{datetime.now()} - Model saved: {model_path}\n")

    # return LOG_FILE




if __name__ == "__main__":
    train_model()

