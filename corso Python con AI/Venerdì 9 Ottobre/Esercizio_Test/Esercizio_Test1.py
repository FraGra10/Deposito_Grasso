
#Funzione per la lista di interi 
def lista_int_operazioni(lista_interi):
    operazione = input("Scegli l'operazione da  eseguire, tra stampa, elimina, modifica: ")

    if(operazione == "stampa"):
        print(lista_interi)
    if(operazione == "elimina"):
        lista_interi.clear()
    if(operazione == "modifica"):
            
        posizione = int(input("Scegli la posizione da modificare: "))
        valore = int(input("Scegli valore da inserire: "))
        lista_interi[posizione] = valore

#Funzione per la lista di stringhe         
def lista_stringhe_operazioni(lista_stringhe):
    operazione = input("Scegli l'operazione da  eseguire, tra stampa, elimina, modifica: ")

    if(operazione == "stampa"):
        print(lista_stringhe)
    if(operazione == "elimina"):
        lista_stringhe.clear()
    if(operazione == "modifica"):
            
        posizione = int(input("Scegli la posizione da modificare: "))
        valore = input("Scegli valore da inserire: ")
        lista_stringhe[posizione] = valore

#Funzione per la lista di bool  
def lista_bool_operazioni(lista_bool):
    operazione = input("Scegli l'operazione da  eseguire, tra stampa, elimina, modifica: ")

    if(operazione == "stampa"):
        print(lista_bool)
    if(operazione == "elimina"):
        lista_bool.clear()
    if(operazione == "modifica"):
            
        posizione = int(input("Scegli la posizione da modificare: "))
        valore = bool(input("Scegli valore da inserire: "))
        lista_bool[posizione] = valore

    
while(True):
    
    lista_interi = [10,20,45,32,10]
    lista_stringhe = ["ciao","corso","python"]
    lista_bool = [True,False,True]
    
    tipo = int(input("Scegli il tipo di lista da considerare: 1,2,3: "))
    
    if(tipo == 1):
        
        lista_int_operazioni(lista_interi)
        
    if(tipo == 2):
        
        lista_stringhe_operazioni(lista_stringhe)
            
    if(tipo == 3):
        
        lista_bool_operazioni(lista_bool)