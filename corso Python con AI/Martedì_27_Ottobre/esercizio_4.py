from sklearn.datasets import load_wine
from sklearn.neighbors import KNeighborsClassifier

wine = load_wine()
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(wine.data, wine.target)                     


test = wine.data[100, :].reshape(1, -1)
print(test)
distanze, indici = knn.kneighbors(test)

print(f"Gli indici dei tre più vicini sono: {indici}")
print(f"Le distanze dei tre più vicini sono: {distanze}")
print("Le classi dei vicini sono:", wine.target[indici])

print("Predizione:", wine.target_names[knn.predict(test)])