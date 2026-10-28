from sklearn.datasets import load_diabetes
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split


X, y = load_diabetes(return_X_y=True)  
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.20,random_state=42)

models =[]
best_score = float("-inf")
best_model = None
models.append(KNeighborsRegressor(n_neighbors=1, weights="uniform"))
models.append(KNeighborsRegressor(n_neighbors=1, weights="distance"))
models.append(KNeighborsRegressor(n_neighbors=5, weights="uniform"))
models.append(KNeighborsRegressor(n_neighbors=5, weights="distance"))
models.append(KNeighborsRegressor(n_neighbors=20, weights="uniform"))
models.append(KNeighborsRegressor(n_neighbors=20, weights="distance"))

for modello in models:

    modello.fit(X_train,y_train)                                       
    #print("score: ", modello.score(X_test, y_test))
    if( modello.score(X_test, y_test) > best_score):
        best_score =  modello.score(X_test, y_test)
        best_model = modello

print("Modello che funziona meglio:")
print("Numero di vicini:", best_model.n_neighbors)
print("Tipo di pesi:", best_model.weights)
print("Lo score più alto è :", best_score)
      