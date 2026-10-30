from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, ConfusionMatrixDisplay, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

X,y = load_digits(return_X_y=True)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3, random_state=42, stratify=y)
albero = DecisionTreeClassifier(max_depth=8, random_state=42).fit(X_train,y_train)

y_pred = albero.predict(X_test)

#Classification report 
print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, albero.predict(X_test))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",              # annot: scrive i numeri nelle celle
            xticklabels=range(10), yticklabels=range(10))
plt.xlabel("Previsto"); plt.ylabel("Reale"); plt.title("Matrice di confusione - albero")
plt.show()



for i in range(len(cm)):
    riga = np.delete(cm[i], i)
    print(f"Cifra {i}: {sum(riga)} errori")