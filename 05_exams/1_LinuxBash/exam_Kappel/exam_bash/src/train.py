"""
-------------------------------------------------------------------------------
This script runs the training of an XGBoost model to predict graphics card sales 
from the preprocessed data.

1. It starts by searching for the latest preprocessed CSV file in the 'data/processed/' directory.
2. If a standard model (model.pkl) does not exist, it loads the data, trains a model,
   evaluates it, and saves it as 'model/model.pkl'.
3. If a standard model already exists, it trains a new model on the latest data,
   evaluates it, and saves the model in the 'model/' folder in the format:
   model_YYYYMMDD_HHMM.pkl.
4. Performance metrics (RMSE, MAE, R²) are displayed and saved in the log file.
5. Any errors are handled and reported in the logs.
-------------------------------------------------------------------------------
"""

import os
import pandas as pd
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from datetime import datetime
import pickle


# Folder dir section
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # one level up

RAW_DIR = os.path.join(ROOT_DIR, "data", "processed")
MODEL_DIR = os.path.join(ROOT_DIR, "model")
LOG_FILE = os.path.join(ROOT_DIR, "logs", "train.logs")

def train_model():
    """
    train the model with xgboost, calclulate metrics into the log file,
    returns filename of the trained model for the log file
    """

    # logging and Foldercheck
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a") as log: 
        log.write(f"{datetime.now()} - Starting training\n")
    

    # latest csv
    files = [f for f in os.listdir(RAW_DIR) if f.endswith(".csv")]    # f.end not forgett
    if not files:
        raise FileNotFoundError("No csv in data/processed")
    #latest csv - Filename Date
    latest = max(files, key=lambda f: os.path.getmtime(os.path.join(RAW_DIR, f)))
    df = pd.read_csv(os.path.join(RAW_DIR, latest))


    # Feature eng.

    if "model" not in df.columns or "sales" not in df.columns:
        raise ValueError("Expected columns 'model' and 'sales' not found.")
    #  
    X = pd.get_dummies(df["model"])             # One-hot encoding
    y = df["sales"]


    # Model training
    model = XGBRegressor()
    model.fit(X, y)

    # Evaluate
    preds = model.predict(X)
    mse = mean_squared_error(y, preds)
    rmse = mse ** 0.5
    mae = mean_absolute_error(y, preds)
    r2 = r2_score(y, preds)

    # Logging metrics
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()} - RMSE: {rmse:.3f}, MAE: {mae:.3f}, R2: {r2:.3f}\n")

    # Save model
    os.makedirs(MODEL_DIR, exist_ok=True)
    standard_model_path = os.path.join(MODEL_DIR, "model.pkl")

    if not os.path.exists(standard_model_path):
        model_path = standard_model_path
    else:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        model_path = os.path.join(MODEL_DIR, f"model_{timestamp}.pkl")

    with open(model_path, "wb") as f:
        pickle.dump(model, f)

    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()} - Model saved: {model_path}\n")


    # mk testing
    # print("\nX head:")
    # print(X.head(10))

    # print("\ny head:")
    # print(y.head(10))

    return model_path



if __name__ == "__main__":
    test = train_model()
    print(test)
