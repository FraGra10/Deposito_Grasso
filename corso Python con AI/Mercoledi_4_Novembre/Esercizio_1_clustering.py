import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import pandas as pd

X, _ = make_blobs(n_samples=400, centers=3, cluster_std=1.00, random_state=7)    # ignoriamo le etichette

k_values  = [3, 2, 5]
sil_score = []

for  i in k_values:
    
    kmeans = KMeans(n_clusters=i, init="k-means++", n_init=10, random_state=42)
    etichette = kmeans.fit_predict(X)                                                # fit + etichetta di ogni punto

    sil_score.append(silhouette_score(X, kmeans.labels_))

    plt.scatter(X[:, 0], X[:, 1], c=etichette, s=30, cmap="viridis")
    plt.scatter(*kmeans.cluster_centers_.T, c="red", s=200, alpha=0.75, marker="X")   # centroidi
    plt.title(f"Clustering con K-Means (k={i})"); plt.show()
    

df = pd.DataFrame({
    "K" : k_values,
    "s_score": sil_score
})
df = df.set_index("K")
print(df)