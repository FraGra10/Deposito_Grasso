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

#######################################################

#Indexing slicing 

arr = np.array([1,2,3,4,5])

#Indexing
print(arr[0])

#Slicing 
print(arr[1:3])

#Boolean Indexing
print(arr[arr < 4])
print("**********************************************************************")
##############################################################################
#Esempio 4

arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

#Slicing sulle righe 
print(arr[1:3])

#Slicing sulle colonne
print(arr[:,1:3])

#Slicign Misto 
print(arr[1:3, 1:3])

print(arr[1:8:2]) # Output: [1 3 5 7]

# Omettere start e stop
print(arr[:5]) # Output: [0 1 2 3 4]
print(arr[5:]) # Output: [5 6 7 8 9]

# Utilizzare indici negativi
print(arr[-5:]) # Output: [5 6 7 8 9]
print(arr[:-5]) # Output: [0 1 2 3 4]