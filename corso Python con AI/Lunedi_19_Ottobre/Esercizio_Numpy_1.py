import numpy as np


arr = np.arange(10,50)

print("I valori contenuti nell'array sono: ", arr)
print("Il tipo di dato contenuto nell'array è: ", arr.dtype)
print("La forma dell'array è: ", arr.shape)


arr = arr.astype(float)
print("Il tipo di dato contenuto nell'array dopo la conversione è: ", arr.dtype)

########################

arr_1 = np.array([[2,1,3,4],[23,12,43,120]])

print("Tipo di dato dell' array è: ", arr_1.dtype)
print("La forma dell'array è: ", arr_1.shape)


