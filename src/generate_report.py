import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Өгөгдөл унших
df = pd.read_csv("data/processed/engineered_data.csv")
X_test = df.drop(columns=["Churn"])
y_test = df["Churn"]

# Загвар унших
model = joblib.load("models/random_forest.pkl")

# Урьдчилан таамаглах
y_pred = model.predict(X_test)

# Үзүүлэлтүүдийг тооцоолох
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Markdown форматтай тайлан үүсгэх
report_content = f"""
# Model Evaluation Report

## Загварын үр дүн:

- **Нарийвчлал (Accuracy):** {accuracy:.2f}
- **Үнэн зөв таамаглал (Precision):** {precision:.2f}
- **Эргэх холбоо (Recall):** {recall:.2f}
- **F1-Score:** {f1:.2f}

## Дүрслэлүүд:
- ![Churn Distribution](figures/churn_distribution.png)
- ![Feature Importance](figures/feature_importance.png)
- ![Confusion Matrix](figures/confusion_matrix.png)

"""

# Тайланг хадгалах
with open("reports/model_evaluation.md", "w", encoding="utf-8") as f:
    f.write(report_content)

print("Загварын үнэлгээний Markdown тайлан үүсгэгдлээ!")
