import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
import numpy as np

digits = load_digits(as_frame=True) 

df = digits.frame       #Generazione di df come frame 
y = digits.target
X = digits.data

#print(X.shape)      #Forma di X 

#print(digits.keys())
'''
fig, axes = plt.subplots(2, 5, figsize=(10, 5))

for i, ax in enumerate(axes.flat):
    ax.imshow(digits.images[i], cmap="gray")
    ax.set_title(f"Cifra: {digits.target[i]}")
    ax.axis("off")

plt.tight_layout()
plt.show()
'''
###################################################

cifre = np.unique(y)

conteggi = []

for cifra in cifre:
    conteggi.append(np.sum(y == cifra))
    
    
plt.bar(cifre, conteggi)
plt.xlabel("Cifra")
plt.ylabel("Numero di campioni")
plt.title("Distribuzione delle cifre")
plt.xticks(cifre)
plt.show()