#Esercizio con while

while(True):
    
    scelta = int(input("Quale esercizio vuoi fare? 1 , 2 , 3; 0 per uscire: "))
    
    
    if(scelta == 1):
        
        lista_numeri = []
        
        while(True):
    
            numero = int(input("Inserisci numero intero:"))
            lista_numeri.append(numero)
    
            if(numero == 0):
                print("La somma dei numeri inseriti è: ", sum(lista_numeri))
                break
    
    if(scelta == 2):
    
    #Esercizio con for
        parola = input("Inserisci una parola: ")

        for lettera in parola:
            print(lettera)
    
    if(scelta == 3):

    #Esercizio con ciclo range

        scelta_max  = int(input("Scegli il massimo numero: "))
        scelta_step = int(input("Scegli lo step: "))

        for i in range(0, scelta_max, scelta_step):
            print(i)

    if(scelta == 0):
        break

    #-------------------------------------------------------------------------
    #Esercizio sulle liste
    
    lista = []
    
    while(True):
        
        scelta = input("Scegli l'operazione da fare , tra: mod,add,rem,see,o exit")
        
        match scelta:
            
            case "see":
                print(lista)
            case "add":
             elemento = input("Inserisci valore da aggiungere")
             lista.append(elemento)
            case "rem":
                lista.clear()
            case "mod":
                if(len(lista) > 0):
                    posizione = int(input("Inserisci la posizione dell'elemento che vuoi modificare"))
                    elemento  = int(input("Scegli elemento da aggiungere"))
                    lista[posizione] = elemento
                else:
                    print("Lista vuota, non modificabile!")
            case "exit":
                break
#------------------------------------------------------------------------------              
                
            