from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

X, y = load_digits(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train,y_train)
print(f"training score: {knn.score(X_train, y_train):.2f}"   # punteggio sui dati visti
f" test score: {knn.score(X_test, y_test):.2f}")                # punteggio su dati nuovi

#Il modello  è in lieve overfitting dal momento che sia il punteggio di training che quello di test sono molto alti:
#100% e 98%. Il modello generalizza molto bene