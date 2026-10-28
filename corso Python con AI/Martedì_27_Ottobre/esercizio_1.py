from sklearn.neighbors import KNeighborsClassifier

# Ogni riga: [peso in kg, altezza in cm]
X = [[14,41],[20,56],[25,51],[45,86],[5,25],[8,28],[9,40],[36,62]]
y = ["gatto", "cane", "cane", "cane", "gatto", "gatto","gatto","cane"]

modello = KNeighborsClassifier(n_neighbors=3)   # 1) istanza con iperparametro
modello.fit(X, y)                               # 2) addestramento

print(modello.predict([[8, 15], [28, 50]]))   # 3) predizione -> ['mela' 'arancia']
print(modello.classes_) 
print(modello.score(X,y)) 