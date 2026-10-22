import matplotlib as mp 

import matplotlib.pyplot as plt


#Grafico a Linea
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.figure()
plt.plot(x, y)

# extra
plt.title('Grafico a Linee')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid()

#plt.show()


#Esempio di Grafico a Barre

categories = ['A','B','C','D','E']
values = [3,7,2,5,8]

plt.figure()
plt.bar(categories,values)
plt.title('Grafico a barre')
plt.xlabel('Categorie')
plt.ylabel('Valori')
plt.show()

#Esempio con istogramma 
import numpy as np

import matplotlib.pyplot as plt


data = np.random.randn(1000)


plt.figure()

plt.hist(data, bins=30) #bins sono vari livelli  utilizzati per creare istogramma

plt.title('Istogramma')

plt.xlabel('Valori')

plt.ylabel('Frequenza')

plt.show()

#Scatter plot 

import numpy as np

import matplotlib.pyplot as plt


x = np.random.rand(50)

y = np.random.rand(50)


plt.figure()

plt.scatter(x, y)

plt.title('Scatter Plot')

plt.xlabel('X Axis')

plt.ylabel('Y Axis')

plt.show()