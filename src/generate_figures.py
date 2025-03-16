import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import joblib
from sklearn.metrics import confusion_matrix
import os

# Хавтас байхгүй бол автоматаар үүсгэх
FIGURE_PATH = "reports/figures/"
os.makedirs(FIGURE_PATH, exist_ok=True)

# Өгөгдөл унших
df = pd.read_csv("data/processed/engineered_data.csv")

# Churn хувь хэмжээ дүрслэх
plt.figure(figsize=(6, 4))
sns.countplot(x="Churn", data=df)
plt.title("Churn хувь хэмжээ")
plt.savefig("reports/figures/churn_distribution.png")  
plt.close()

# Загвар унших
model = joblib.load("models/random_forest.pkl")

# Онцлог шинжүүдийн ач холбогдлыг авах
feature_importance = model.feature_importances_
feature_names = df.drop(columns=["Churn"]).columns

# Онцлог шинжийн ач холбогдлыг дүрслэх
plt.figure(figsize=(10, 6))
sns.barplot(x=feature_importance, y=feature_names)
plt.title("Онцлог шинжүүдийн ач холбогдол")
plt.savefig("reports/figures/feature_importance.png")  
plt.close()

# Confusion Matrix дүрслэх
y_test = df["Churn"]
y_pred = model.predict(df.drop(columns=["Churn"]))
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.xlabel("Таамагласан утга")
plt.ylabel("Бодит утга")
plt.title("Confusion Matrix")
plt.savefig("reports/figures/confusion_matrix.png")  
plt.close()

print("Дүрслэлүүд амжилттай хадгалагдлаа!")
