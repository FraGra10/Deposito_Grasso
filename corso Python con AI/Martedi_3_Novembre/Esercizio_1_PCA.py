import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

wine = load_wine()
X_scaled = StandardScaler().fit_transform(wine.data) 

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)                     

print("Varianza spiegata:", pca.explained_variance_ratio_.round(3))         
print("Totale conservato:", pca.explained_variance_ratio_.sum().round(3))

plt.scatter(X_pca[:, 0], X_pca[:, 1], c=wine.target, cmap="plasma", edgecolor="k")
plt.xlabel("Prima componente principale"); plt.ylabel("Seconda componente principale")
plt.title("Wine dopo la PCA"); plt.show()

### senza scaling 

pca_2 = PCA(n_components = 2)
X_pca_2 = pca_2.fit_transform(wine.data)
print("Varianza spiegata:", pca_2.explained_variance_ratio_.round(3))         
print("Totale conservato:", pca_2.explained_variance_ratio_.sum().round(3))

plt.scatter(X_pca_2[:, 0], X_pca_2[:, 1], c=wine.target, cmap="plasma", edgecolor="k")
plt.xlabel("Prima componente principale"); plt.ylabel("Seconda componente principale")
plt.title("Wine dopo la PCA_2")
plt.show()

print(pca_2.components_[0])
print(wine.feature_names)

#La feature che domina la PCA non scalata è proline perchè ha la scala molto più grande rispetto a tutte le altre 
#features