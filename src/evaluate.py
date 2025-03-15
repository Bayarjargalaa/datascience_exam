import logging
from logger import training_logger
import joblib
from sklearn.metrics import accuracy_score, classification_report

def evaluate_model(X_test, y_test):
    """Загварын гүйцэтгэлийг шалгах"""
    try:
        training_logger.info("🔵 Загварын үнэлгээ эхэлж байна...")
        
        # Загвар унших
        model = joblib.load("models/random_forest.pkl")
        
        # Урьдчилан таамаглах
        y_pred = model.predict(X_test)
        
        # Нарийвчлал
        accuracy = accuracy_score(y_test, y_pred)
        training_logger.info(f"Загварын нарийвчлал: {accuracy:.2f}")

        # Илүү дэлгэрэнгүй тайлан
        report = classification_report(y_test, y_pred)
        training_logger.info(f"Загварын тайлан: \n{report}")

    except Exception as e:
        training_logger.error(f"Загварын үнэлгээнд алдаа гарлаа: {str(e)}")
