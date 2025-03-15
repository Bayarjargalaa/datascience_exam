import logging
from logger import pipeline_logger
import pandas as pd

def load_data():
    """CSV өгөгдлийг унших"""
    try:
        pipeline_logger.info("Өгөгдөл ачаалж байна...")
        
        df = pd.read_csv("data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")
        pipeline_logger.info("Өгөгдөл амжилттай ачаалагдлаа.")

        return df
    except Exception as e:
        pipeline_logger.error(f"Өгөгдөл уншихад алдаа гарлаа: {str(e)}")
        return None
