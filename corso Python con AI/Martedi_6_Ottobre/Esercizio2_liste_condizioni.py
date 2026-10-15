#Esercizio sulle liste 

lista_numeri = [10,21,34,45,76,23,3,0]

lista_parole = ["andare","pizza","barca","mare"]

num_lista =  int(input("Quale lista vuoi scegliere?"))

#scelta delle operazioni da compiere sulle liste
operazione = input("Vuoi aggiungere o rimuovere un elemento?")

if(operazione == "aggiungere"):
   
    val = input("Indica elemento da aggiungere alla lista: ")
    
    if(num_lista == 1) :
        lista_numeri.append(val)
    elif(num_lista == 2):
        lista_parole.append(val)
    else:
        print("Lista non trovata!")    
    
elif(operazione == "rimuovere"):
    
    if(num_lista ==1 ):
        lista_numeri.pop(1)
    elif(num_lista == 2):
        lista_parole.pop(1)
    else:
        print("Lista non trovata!")
else:
    print("Operazione non consentita!")
    
#print della lista modificata
if(num_lista == 1):
    print(lista_numeri)
elif(num_lista == 2):
    print(lista_parole)
else:
    print("Lista non trovata!")
    
    