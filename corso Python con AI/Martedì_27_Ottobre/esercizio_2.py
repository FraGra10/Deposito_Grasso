from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


X, y = load_breast_cancer(return_X_y=True)                                   # 1) dati

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25,random_state=0)

modello = KNeighborsClassifier(n_neighbors=3)  
modello.fit(X_train,y_train)                                        # 4) scelta del modello
y_pred = modello.predict(X_test)                                    # 6) predizione sul test

print("accuracy_score:", accuracy_score(y_test, y_pred))            # 7) valutazione
print("score:         ", modello.score(X_test, y_test))             # stesso valore

if(accuracy_score(y_test, y_pred) ==  modello.score(X_test, y_test)):
    print("accuracy_score e modello.score coincidono!")
else:
    print("accuracy e score non coincidono!")
    
print(f"Classi: {modello.classes_}")

print(f"Features: {modello.n_features_in_}")
   