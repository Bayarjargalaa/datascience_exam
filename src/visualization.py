import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

# Тайлан хадгалах фолдер үүсгэх
FIGURE_PATH = "reports/figures/"
os.makedirs(FIGURE_PATH, exist_ok=True)

def load_data():
    """Өгөгдлийг ачаалж унших"""
    df = pd.read_csv("data/processed/engineered_data.csv")
    return df

def plot_histogram(df):
    """Total Charges-ийн тархалтын график"""
    plt.figure(figsize=(8,5))
    plt.hist(df["TotalCharges"].dropna(), bins=30, color="blue", alpha=0.7)
    plt.title("Total Charges-ийн тархалт")
    plt.xlabel("Total Charges")
    plt.ylabel("Тоон хэмжээ")
    plt.grid(True)
    plt.savefig(FIGURE_PATH + "histogram.png")
    plt.close()

def plot_churn_distribution(df):
    """Churn хувь хэмжээг харуулах баганан график"""
    plt.figure(figsize=(6,4))
    sns.countplot(x="Churn", hue="Churn", data=df, palette="coolwarm", legend=False)
    plt.title("Churn хувь хэмжээ")
    plt.xlabel("Churn")
    plt.ylabel("Тоон хэмжээ")
    plt.savefig(FIGURE_PATH + "churn_distribution.png")
    plt.close()

def plot_boxplot(df):
    """Churn болон Total Charges харьцуулсан Boxplot"""
    plt.figure(figsize=(8,5))
    sns.boxplot(x="Churn", y="TotalCharges", data=df)
    plt.title("Total Charges vs Churn")
    plt.savefig(FIGURE_PATH + "boxplot.png")
    plt.close()

def plot_correlation_heatmap(df):
    """Корреляцийн зураглал (Heatmap)"""
    plt.figure(figsize=(10,6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Корреляцийн зураглал")
    plt.savefig(FIGURE_PATH + "correlation_heatmap.png")
    plt.close()

def plot_pie_chart(df):
    """Churn хувь хэмжээг харуулах Pie Chart"""
    fig = px.pie(df, names="Churn", title="Churn хувь хэмжээ", hole=0.4)
    fig.write_image(FIGURE_PATH + "pie_chart.png")

def plot_scatter(df):
    """Monthly Charges vs Total Charges харьцуулсан Scatter Plot"""
    fig = px.scatter(df, x="MonthlyCharges", y="TotalCharges", color="Churn",
                     title="Monthly Charges vs Total Charges", opacity=0.7)
    fig.write_image(FIGURE_PATH + "scatter_plot.png")

def generate_visualizations():
    """Бүх графикийг үүсгэж хадгалах"""
    print("📊 Дүрслэлүүд үүсгэж байна...")
    
    df = load_data()
    
    plot_histogram(df)
    plot_churn_distribution(df)
    plot_boxplot(df)
    plot_correlation_heatmap(df)
    plot_pie_chart(df)
    plot_scatter(df)

    print("Бүх дүрслэл `reports/figures/` фолдерт хадгалагдлаа!")

if __name__ == "__main__":
    generate_visualizations()
