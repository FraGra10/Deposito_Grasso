import numpy as np
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

X, y = make_circles(n_samples=500, noise=0.25, factor=0.5, random_state=0)

#Divisione Dataset in due gruppi 
X_temp, X_test, y_temp, y_test = train_test_split(X,y, test_size=0.2, random_state=0)

#Ulteriore divisione del dataset per la validazione di k 
X_train, X_val, y_train, y_val = train_test_split(X_temp,y_temp, test_size=0.25, random_state=0)


best_k = 0 
best_val = 0
# Ricerca del miglior valore di k in base alla miglior accuratezza sul dataset di validazione
for k in range(1,51,2):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train,y_train)
    val = knn.score(X_val,y_val)
    if(val > best_val):
        best_val = val
        best_k = k 

#misura del'accuratezza finale sul dataset knn_2 
knn_2 = KNeighborsClassifier(n_neighbors= best_k)
knn_2.fit(X_train,y_train)
print("k scelto:", best_k, " validation:", round(best_val, 3))
print("Accuratezza finale sul test:", round(knn_2.score(X_test, y_test), 3))