import numpy as np 

#array con linspace
array_lin = np.linspace(0,1,12)

#reshape

array_reshape = np.reshape(array_lin,(3,4))
print(array_reshape)

#random array
random_arr = np.random.rand(3,4)
print(random_arr)


#print
print("La somma degli elementi della matrice iniziale è pari a :", np.sum(array_reshape))
print("La somma degli elementi della matrice random è pari a :", np.sum(random_arr))

print("I valori della matrice ottenuta con linspace convertiti a int sono: ", np.astype(array_lin,int))