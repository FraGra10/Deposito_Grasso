from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, export_text

wine = load_wine()
albero = DecisionTreeClassifier(max_depth=2, random_state=42)   # massimo 2 domande in sequenza
albero.fit(wine.data, wine.target)

print(export_text(albero, feature_names=wine.feature_names))     # le regole imparate

#Se proline è maggiore di 755 e flavanoids è maggiore di 0 , allora il modello assegna la classe 0 