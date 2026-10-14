#Definizione classe madre 
class Posto:

    def __init__(self, numero , fila ):
       
       self.__occupato = False
       self.__numero   = numero 
       self.__fila     = fila 
       
    def prenota(self):
        
        if(self.__occupato == False):
            print("Posto prenotato!")
            self.__occupato = True 
        else:
            print("Posto già occupato!")
    
    def libera(self):
        
        if(self.__occupato == True):
            print("Posto liberato!")
            self.__occupato = False
        else:
            print("Posto già libero!")
    
    def get_numero(self):
        return self.__numero
    def get_fila(self):
        return self.__fila
    def get_occupato(self):
        return self.__occupato
            
    def set_occupato(self, stato):
        
        self.__occupato = stato   
        
        
#Classe Derivata Posto Standard 
class PostoStandard(Posto):
    
    def __init__(self,numero,fila,costo):
        super().__init__(numero,fila)
        self.__costo = costo
        
    
    def get_numero(self):
        return self.__costo
    
    
    def prenota(self):
        
        if(self.__occupato == False):
            print("Prenotazione online effettuata!")
            print("Costo di prenotazione pari a ", self.__costo, "Euro")
            self.set_occupato(True)
        else:
            print("Posto già occupato, impossibile proseguire con la prenotazione!")
    
    
##### classe Teatro 

class Teatro:
    
    def __init__(self):
        self.__posti = []

#Funzione per aggiungere il posto 
    def aggiungi_posto(self,obj):
        self.__posti.append(obj)
        
#Funzione per prenotare il posto 
    def prenota_posto(self,numero,fila):
        
        for i in self.__posti:
            if(self.__posti[i].get_numero == numero and self.__posti[i].get_fila == fila ):
                print("Posto trovato!")
                self.__posti[i].prenota()
    
#Funzione per stampare posti occupati 
    def stampa_posti_occupati(self):
        
        for i in self.__posti:
            if(self.__posti[i].get_occupato == True ):
                print(f"Posto {self.__posti[i].get_numero} occupato!")
                
