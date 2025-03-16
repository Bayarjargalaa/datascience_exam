import logging
from logger import training_logger
from sklearn.ensemble import RandomForestClassifier
import joblib

import os
os.makedirs("models", exist_ok=True)


def train_model(X_train, y_train):
    """RandomForestClassifier загвар сургах"""
    try:
        training_logger.info("Загварын сургалт эхэллээ...")
        
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        # Загвар хадгалах
        joblib.dump(model, "models/random_forest.pkl")
        return model

        training_logger.info("Загвар амжилттай сурлаа.")
    except Exception as e:
        training_logger.error(f"Загвар сургалтын явцад алдаа гарлаа: {str(e)}")
