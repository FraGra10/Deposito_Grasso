#Definizione classe Prodotto

class Prodotto:
    
    def __init__(self,nome,costo_produzione,prezzo_vendita):
        
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita  = prezzo_vendita
        
    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione

#Definizione classi derivate con modifica del costruttore   
class Elettronica(Prodotto):
    
    def __init__(self,nome,costo_produzione,prezzo_vendita,garanzia):
        
        super().__init__(nome,costo_produzione,prezzo_vendita)
    
        self.garanzia = garanzia 
        

class Abbigliamento(Prodotto):
    
    def __init__(self,nome,costo_produzione,prezzo_vendita,materiale):
        
        super().__init__(nome,costo_produzione,prezzo_vendita)
    
        self.garanzia = materiale 

#-------------------------------------------------        

#Definizione classe Fabbrica con due elementi e i relativi prezzi 
class Fabbrica:
    
    def __init__(self):
        
        self.numero_polo = []
        self.numero_smartphone = []
        self.prezzi_polo =[]
        self.prezzi_smartphone = []
        
    
    #Aggiungi prodotto all'inventario a seconda che sia polo o smartphone
    def aggiungi_prodotto(self):
        
        elemento = input("Quale elemento vuoi aggiungere? polo o smartphone?")

        if(elemento == "polo"):
            elemento = input("Inserisci marca dell'elemento da aggiungere: ")
            prezzo = int(input("Inserisci il prezzo dell'elemento: "))
            self.numero_polo.append(elemento)
            self.prezzi_polo.append(prezzo)
            
            
        if(elemento == "smartphone"):
            elemento = input("Inserisci marca dell'elemento da aggiungere: ")
            self.numero_smartphone.append(elemento)
            self.prezzi_smartphone.append(elemento)
            
    
    #Vendo prodotto a seconda che sia smartphone o polo
    def vendi_prodotto(self):
        elemento = input("Quale elemento vuoi vendere? : ")
        
        if(elemento == "polo"):
            self.numero_polo.pop()
            print(f"Profitto pari a: {self.prezzi_polo[-1]}")
            self.prezzi_polo.pop()
        if(elemento == "smartphone"):
            self.numero_polo.pop()
            print(f"Profitto pari a: {self.prezzi_smartphone[-1]}")
            self.prezzi_smartphone.pop()
            
    #Reinserisco nell'inventario a seconda che sia polo o smartphone
    def resi_prodotto(self):
        
        elemento = input("Quale elemento vuoi restituire? : ")
        if(elemento == "polo"):
            elemento = input("Inserisci marca dell'elemento da aggiungere: ")
            self.numero_polo.append(elemento)
            prezzo = int(input("Indica il prezzo a cui reinserirlo: "))
            self.prezzi_polo.append(prezzo)
        if(elemento == "smartphone"):
            elemento = input("Inserisci marca dell'elemento da aggiungere: ")
            self.numero_smartphone.append(elemento)
            prezzo = int(input("Indica il prezzo a cui reinserirlo: "))
            self.prezzi_smartphone.append(prezzo)
        
        
#----------------------------------------------------------------------------------------------------



Smartphone = Elettronica("Cellulare",10,20,"2026")
T_shirt = Abbigliamento("Maglia",2,5,"sintetico")

print(T_shirt.calcola_profitto())