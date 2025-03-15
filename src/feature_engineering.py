from sklearn.preprocessing import LabelEncoder

def encode_categorical_columns(df):
    """Бүх категори өгөгдлийг тоон утгад хөрвүүлэх"""
    label_encoders = {}
    for col in df.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le
    return df, label_encoders
