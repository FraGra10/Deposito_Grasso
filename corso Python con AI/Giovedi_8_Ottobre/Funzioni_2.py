#Generatori
# def conta_fino_a(numero_massimo):


#Decoratore 

def dec(funzione):
    def wrapper():
        print("Prima dell'esecuzione della funzione")
        funzione()
        print("Dopo dell'esecuzione della funzione")
    return wrapper

@dec
def saluta():
    print("saluta!")
    

saluta()