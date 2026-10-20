import numpy as np


#Creazione array
array_1 = np.arange(0,50) 
array_2 = np.random.randint(49,102,50)

array_c = np.concatenate((array_1,array_2))

print("L'array risultante è pari a : ", array_c)
print("Il tipo degli elementi dell'array è: ", array_c.dtype)
print("La forma dell'array è:", array_c.shape)

#Modifica del tipo di dato dell'array 
array_c = np.astype(array_c,np.float64)

print("Dopo la conversione, il tipo degli elementi dell'array è: ", array_c.dtype)
print("Dopo la conversione, la forma dell'array è:", array_c.shape)

#Primi 10 elementi

array_c_0_10 = array_c[0:10]

print("I primi 10 elementi dell'array sono: ", array_c_0_10)

#Ultimi 7 elementi

array_c_7 = array_c[-7:]

print("Gli ultimi 7 elementi dell'array sono: ", array_c_7)

#Stampa degli elementi dall'indice 5 all'indice 20 
array_c_5_20 = array_c[5:20]
print("Gli elementi dell'array dall'indice 5 al 20 sono:", array_c_5_20)

#Stampa di ogni quarto elemento dell'array 

array_c_4 = array_c[::4]

print("I valori dell'array distanziati di 4, sono: ", array_c_4)

#Modifica tramite slicing degli elementi 

array_c_999 = array_c
array_c_999[10:15] = 999

print("L'array modificato è: ", array_c_999)

#Utilizzo Fancy Indexing 

array_c_pos = array_c[[0,3,7,12,25,33,48]]

print("L'array ottenuto con fancy indexing è: ", array_c_pos)

# elementi pari 

array_c_pari  = array_c[array_c%2 == 0]

print("L'array ottenuto considerando solo gli elementi pari è: \n ", array_c_pari)

#elementi superiori alla media dell'array 

array_c_media  = array_c[ array_c > np.average(array_c)]

print("L'array ottenuto considerando solo gli elementi maggiori della media è: \n ", array_c_media)




