import numpy as np 


def main_function():
#array con linspace
    array_lin = np.linspace(0,10,50)

#array con random
    array_ran = np.random.random(50)

#sommo i due array precedenti 
    array_2 = array_lin + array_ran

#somma degli elementi del precedente array 
    array_sum  = np.sum(array_2)

#somma degli elementi del precedente array maggiori di 5
    array_sum_2 = np.sum(array_2[array_2 > 5])

#Print 
###########################################################
    print("L'array generato con linspace è: ", array_lin)

    print("L'array generato con random è: ", array_ran)

    print("Il nuovo array risultante dalla somma è: ", array_2)

    print("La somma degli elementi dell'array risultante dalla somma è: ", array_sum)

    print("La somma degli elementi dell'array risultante dalla somma, maggiori di 5 è:", array_sum_2)


    operazione = input("Vuoi sovrascrivere il txt?: S,N ")
    
    if(operazione.lower() == "s"): 
        
        with open("array.txt", "a") as file:

            file.write("L'array generato con linspace è:\n")
            file.write(str(array_lin) + "\n")

            file.write("L'array generato con random è:\n")
            file.write(str(array_ran) + "\n")

            file.write("Il nuovo array risultante dalla somma è:\n")
            file.write(str(array_2) + "\n")

            file.write("La somma degli elementi dell'array risultante dalla somma è:\n")
            file.write(str(array_sum) + "\n")

            file.write("La somma degli elementi dell'array risultante dalla somma, maggiori di 5 è:\n")
            file.write(str(array_sum_2) + "\n")
            
    if(operazione.lower() == "n"): 
        
        with open("array.txt", "w") as file:

            file.write("L'array generato con linspace è:\n")
            file.write(str(array_lin) + "\n")

            file.write("L'array generato con random è:\n")
            file.write(str(array_ran) + "\n")

            file.write("Il nuovo array risultante dalla somma è:\n")
            file.write(str(array_2) + "\n")

            file.write("La somma degli elementi dell'array risultante dalla somma è:\n")
            file.write(str(array_sum) + "\n")

            file.write("La somma degli elementi dell'array risultante dalla somma, maggiori di 5 è:\n")
            file.write(str(array_sum_2) + "\n")
            
    print("Risultati salvati nel file array.txt")





while(True):
    
    operazione = input("Inserisci 1 per ripetere il processo, 2 per uscire: ")
    
    if(operazione == "1"):
        
        main_function()
    
    else:
        break