import numpy as np 




#Definizione dell'array
arr = np.random.randint(10,50,20)
print("I valori dell'array sono: ", arr)

#Primi dieci elementi
first_ten_elem = arr[0:10]
print("I primi dieci elementi sono: ", first_ten_elem)

#Ultimi cinque elementi
last_five_elem = arr[-5:]
print("Gli ultimi cinque elementi sono: ", last_five_elem)

#Dall'indice 5 al 15

slicing_5_15 = arr[5:15]
print("Gli elementi dal  cinque al quindici sono: ", slicing_5_15)

#Utilizzo dello slicing per estrarre ogni terzo elemento dell'array 

slicing_3 = arr[::3]

print("Gli elementi estratti ogni tre passi sono: ", slicing_3)


#modifica elementi

mod = arr 
mod[5:10] = 99
print("Gli elementi dell'array modificato sono: ", mod)