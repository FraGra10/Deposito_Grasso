import numpy as np


arr = np.array([1,2,3,4,5])

arr2d = np.array([[1,2,3], [4,5,6]])


print("Valore massimo: ", arr2d.max())

#Per vedere il tipo di dati:
print("Il tipo dei dati dell'array è: ", arr2d.dtype )
#Per vedere il numero di righe e di colonne dell'array:
print("Forma dell'array: ", arr2d.shape)

#arange serve per creare un array direttamente nel contesto di numpy senza passare da fuori (  è come il range)
arr = np.arange(10)

#reshape cambia la forma di un array senza modificarne i dati
#Può essere eseguito solo su comportamento che hanno senso, non posso fare reshape con più posizioni di quelle dell'array principale
arr = np.arange(6)
reshaped_arr = arr.reshape((2,3))
print(reshaped_arr)


