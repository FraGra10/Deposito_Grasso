'''
#Esempio classe con funzione speciale __str__
class Studente:
    
    def __init__(self,nome,eta):
        self.nome = nome
        self.eta = eta 
        
    def __str__(self):
        return "Studente: " + self.nome + ", età, " + str(self.eta)
    
    
    
Studente_1 = Studente("Luca", 20)
print(Studente_1)
'''
#--------------------------------------------
'''
#Esempio classe con funzione speciale __len__
class Squadra: 
    
    def __init__(self,nome,giocatori):
        self.nome = nome
        self.giocatori = giocatori
        
    def __len__(self):
        return len(self.giocatori)
    

squadra1 = Squadra("Tigri", ["Luca", "Marco", "Anna"])

print(len(squadra1))
'''
#---------------------------------------------------------------

#Esempio di classe con la funzione speciale call
class Moltiplicatore:
    
    def __init__(self,numero):
        self.numero = numero 
    
    def __call__(self,valore):
        return valore*self.numero
    
doppio = Moltiplicatore(2)

print(doppio(10))