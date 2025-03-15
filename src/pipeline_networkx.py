import networkx as nx
import matplotlib.pyplot as plt

def draw_pipeline():
    G = nx.DiGraph()

    # 🏗 Алхамуудыг нэмэх
    steps = [
        ("Өгөгдөл ачаалах", "Өгөгдөл цэвэрлэх"),
        ("Өгөгдөл цэвэрлэх", "Онцлог шинж боловсруулах"),
        ("Онцлог шинж боловсруулах", "Машин сургалт"),
        ("Машин сургалт", "Загвар үнэлэх"),
        ("Загвар үнэлэх", "Тайлан үүсгэх")
    ]

    G.add_edges_from(steps)

    plt.figure(figsize=(8,5))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")
    
    plt.title("Data Science Pipeline")
    plt.savefig("reports/pipeline_networkx.png")
    # plt.show()

if __name__ == "__main__":
    draw_pipeline()
