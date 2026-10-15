from abc import ABC, abstractmethod

#Implementazione classa astratta 
class Impiegato(ABC):
    
    def __init__(self,nome,cognome,stipendio_base):
    
        self.nome = nome
        self.cognome = cognome
        self.stipendio_base = stipendio_base 

    @abstractmethod
    def calcola_stipendio(self):
        pass 

#Implementazione classe figlia 
class Impiegato_Fisso(Impiegato):
    
    def __init__(self,nome,cognome,stipendio_base):
          
        super().__init__(nome,cognome,stipendio_base)
        
    
    def calcola_stipendio(self):
        
        print(f"Lo stipendio di questo impiegato è pari a quello base, ovvero: {self.stipendio_base}")

#Implementazione classe figlia   
class Impiegato_Proviggione(Impiegato):
    
    def __init__(self,nome,cognome,stipendio_base):
          
        super().__init__(nome,cognome,stipendio_base)
        
    
    def calcola_stipendio(self):
        
        bonus = int(input("Inserisci bonus in euro ottenuto dalle vendite: "))
        print(f"Lo stipendio di questo impiegato è pari a quello base più un bonus relativo alle vendite", self.stipendio_base + bonus)
    
        
    
prova_1 = Impiegato_Fisso("Luciano","Ligabue", 400)
prova_2 = Impiegato_Proviggione("Mario", "Rossi", 100)

prova_1.calcola_stipendio()
prova_2.calcola_stipendio()

def stampa_info(obj_1,obj_2):
    pass