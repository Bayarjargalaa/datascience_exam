import logging
from logger import pipeline_logger
from data_loader import load_data
from feature_engineering import encode_categorical_columns
from model import train_model
from evaluate import evaluate_model
from generate_all_reports import generate_reports 
from pipeline_networkx import draw_pipeline
from visualization import generate_visualizations

from sklearn.model_selection import train_test_split

try:
    pipeline_logger.info("Pipeline эхэлж байна...")

    # Өгөгдлийг ачаалах
    df = load_data()
    pipeline_logger.info("Өгөгдөл ачааллаа.")

    # Категори өгөгдлийг хөрвүүлэх
    df, label_encoders = encode_categorical_columns(df)
    pipeline_logger.info("Категори өгөгдлийг хувиргалаа.")

    # Өгөгдлийг сургалт, тестийн хэсэгт хуваах
    X = df.drop(columns=["Churn"])
    y = df["Churn"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    pipeline_logger.info("Өгөгдөл хуваах амжилттай.")

    # Загвар сургах
    train_model(X_train, y_train)

    # Загвар үнэлэх
    evaluate_model(X_test, y_test)
    
    # Pipeline зураг үүсгэх
    draw_pipeline()
    
    # Дүрслэлүүдийг үүсгэх
    generate_visualizations()

    # Тайлан үүсгэх
    generate_reports()
    pipeline_logger.info("Тайлан амжилттай үүсгэгдлээ.")

    pipeline_logger.info("Pipeline амжилттай дууслаа.")

except Exception as e:
    pipeline_logger.error(f"Pipeline алдаа гарлаа: {str(e)}")
