
#Classe madre 
class UnitaMilitare():
    
    def __init__(self,nome,numero_soldati):
        
        self.nome = nome
        self.numero_soldati = numero_soldati
        
    def muovi(self):   
        print("Unità in movimento!")
        
    def attacca(self):
        print("L'unità si prepara all'attacco!")
        
    def ritira(self):  
        print("Unità in ritirata!")
 
 ############################################################
 #Classi derivate
 
class Fanteria(UnitaMilitare):
    
    def costruisci_trincea(self):
        print("Costruzione difese temporanee!")
    
class Artiglieria(UnitaMilitare):
    
    def calibra_artiglieria(self):
        print("Calibrando i pezzi dell'artiglieria...")

class Cavalleria(UnitaMilitare):
    
    def esplora_terreno(self):
        print("Esplorazione dell'area in corso!")
        
class SupportoLogistico(UnitaMilitare):
    
    def rifornisci_unità(self):
        print("Rifornimenti in arrivo!")
        
class Ricognizione(UnitaMilitare):
    
    def conduci_ricognizione(self):
        print("Missioni di sorveglianza in corso!")     
############################################################
        
#La seguente classe eredita da tutte le precedenti classi 
class ControlloMilitare(Fanteria,Artiglieria,Cavalleria,SupportoLogistico,Ricognizione):

    def __init__(self,nome,numero_soldati):
        
        UnitaMilitare.__init__(self,nome,numero_soldati)
        
        self.nomi_unita =     []
        self.num_soldati = []
    
    def registra_unita(self,nome,numero):
        
        nome = input("Aggiungi il nome dell'unità: ")
        numero = int(input("Quale è il numero dell'unità?"))
        
        self.nomi_unita.append(nome)
        self.num_soldati.append(numero)

    def mostra_unita(self):
        
        print("Le unita presenti sono: ", self.nomi_unità)
    
    def dettagli_unita(self):
        
        print("Il numero di soldati delle unità sono:", self.num_soldati)

#Funzioni speciali implementate: eq, repr, get_attribute
        
    def __eq__(self, value):
        return  self.nome == value.nome and self.num_soldati == value.num_soldati
    
    def __repr__(self):
        return f"Nome dell'unità: {self.nome} Numero di unità: {self.numero_soldati}"
    
    def __getattribute__(self, name_attribute):
        return "Impossibile accedere a dati militari!"
        

Unita_1 = ControlloMilitare("Brigata Sassari",100)
Unita_2 = ControlloMilitare("Gruppo Alpino",100)
Unita_3 = ControlloMilitare("Brigata Sassari",100)

print(Unita_1)
