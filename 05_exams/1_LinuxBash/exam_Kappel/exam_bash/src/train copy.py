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

# Project root
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DIR = os.path.join(ROOT_DIR, "data", "processed")
MODEL_DIR = os.path.join(ROOT_DIR, "model")
LOG_FILE = os.path.join(ROOT_DIR, "logs", "train.logs")


def train_model():

    # Logging
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()} - Starting training\n")

    # Find latest processed CSV
    files = [f for f in os.listdir(RAW_DIR) if f.endswith(".csv")]
    if not files:
        raise FileNotFoundError("No CSV files found in processed folder.")

    latest = max(files, key=lambda f: os.path.getmtime(os.path.join(RAW_DIR, f)))
    df = pd.read_csv(os.path.join(RAW_DIR, latest))

    # Feature engineering
    if "model" not in df.columns or "sales" not in df.columns:
        raise ValueError("Expected columns 'model' and 'sales' not found.")

    X = pd.get_dummies(df["model"])   # One-hot encoding
    y = df["sales"]

    # Train model
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
        log.write(f"{datetime.now()} - RMSE: {rmse:.4f}, MAE: {mae:.4f}, R2: {r2:.4f}\n")

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

    return model_path


if __name__ == "__main__":
    train_model()