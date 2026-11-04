import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

import pandas as pd

iris = load_iris()
X_scaled = StandardScaler().fit_transform(iris.data)

k_values =  list(range(2, 9))

inr_score = []
sil_score = []

for i in k_values:
    kmeans = KMeans(n_clusters=i, init="k-means++", n_init=10, random_state=42).fit(X_scaled)
    sil_score.append(silhouette_score(X_scaled, kmeans.labels_))
    inr_score.append(kmeans.inertia_)

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
axes[0].plot(k_values,  inr_score, "o-"); axes[0].set_title("Metodo del gomito"); axes[0].set_xlabel("k")
axes[1].plot(k_values,  sil_score, "o-"); axes[1].set_title("Silhouette media"); axes[1].set_xlabel("k")
plt.show()

#print(inr_score)
#print("")
#print(sil_score)    

#Il metodo del gomito suggerisce k = 3; Silhouette media suggerisce k = 2; i due metodi non concordano
#Il metodo del gomito suggerisce un valore che coincide con il numero delle specie reali.     