from abc import ABC, abstractmethod
#abbiamo importato una classe e un decoratore



class Pippo_Astratto(ABC):
    
    x= 10 
    
    @abstractmethod
    def Metodoobbligatorio(self):
        pass
    
    def saluta(self):
        print("Saluta!")

class Pippo_Reale(Pippo_Astratto):
    
    def Metodoobbligatorio(self):
        print("Sono reale!")


P_r = Pippo_Reale()
#scritto così non funzionerà, pippo reale DEVE IMPLEMENTARE E SOVRASCRIVERE IL METODO OBBLIGATORIO
#Non si può creare un oggetto di una classe astratta
