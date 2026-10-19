import numpy as np 

#Matrice casuale

arr2d = np.random.randint(0,100,size = (6,6))

print("La matrice casuale è: \n", arr2d)

#Estrazione sottomatrice centrale 

central_matrix =  arr2d[1:5,1:5]

print("La sottomatrice centrle 4x4 è: \n", central_matrix)

#Inversione righe della matrice estratta 

inv_righe_matrix = np.zeros_like(central_matrix) 

for i in range(central_matrix.shape[0]):
    
    inv_righe_matrix[i] = central_matrix[central_matrix.shape[0] - i -1]

    

print(inv_righe_matrix)
    
inv_righe_matrix = (central_matrix[::-1])

print("La sottomatrice invertita è: \n", inv_righe_matrix)
#diagonale principale 

diag = []
for x in range(inv_righe_matrix.shape[0]):
    diag.append(int(inv_righe_matrix[x,x]))
    
print("La diagonale principale della matrice invertita è: ", diag)

#Modifica valori multipli di 3 

inv_2 = inv_righe_matrix
for x in range(inv_2.shape[0]):
    for y in range(inv_2.shape[1]):
        if(inv_2[x,y]%3 == 0):
            inv_2[x,y] = -1 

print("Matrice invertita modificata: \n", inv_2)


