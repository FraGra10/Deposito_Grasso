'''class Francesco():
    
    def __init__(self,eta):
        self.eta = eta
        
    nome = "Francesco"
    
    def saluta(self):
        return ("Ciao a tutti! Io sono", self.nome, "ed ho", self.eta, "anni")
    
eta = 31
Ogg_1 = Francesco(eta)
print(Ogg_1.saluta())
'''

class Automobile():                   #dichiaro la classe
    
    numero_di_ruote = 4               #attributo della classe 
    
    def __init__(self,marca,modello): #metodo costruttore
        self.marca = marca            #attributo di istanza
        self.modello = modello        #attributo di istanza
        
    def stampa_info(self):            #metodo di istanza
        print("L'automobile è una ", self.marca, self.modello)
        
    
#-----------------------------------------------------------------    

Auto_1 = Automobile("Fiat","500")
Auto_2 = Automobile("BMW","X3")
Auto_1.stampa_info()
Auto_2.stampa_info()


#Esempio Metodo Statico


class Calcolatrice():
    
    @staticmethod
    def somma(a,b):
        return a+b
    
    
risultato = Calcolatrice.somma(2,3)
print(risultato)


#-----------------------------------------------------------------
#Esempio metodo di classe 

class Contatore:
    numero_istanze = 0
    
    def __init__(self):
        Contatore.numero_istanze += 1
        
    @classmethod
    def mostra_numero_istanze(cls):
        print("Sono state create", cls.numero_istanze, "istanze.")


c1 = Contatore() 
c2 = Contatore()

Contatore.mostra_numero_istanze()