
# Esercizio su static methods

class Convertitore: 
    
    #funzione per ottenere dollari a partire da euro 
    @staticmethod
    def euro_in_dollari(euro):
        return euro*1.08


    #funzione per ottenere miglia a partire da km
    @staticmethod
    def km_in_miglia(km):
        return km*0.621371
    
    

print("10 Euro corrispondono a: ", Convertitore.euro_in_dollari(10), "dollari")
print("20 Km corrispondono a: ", Convertitore.km_in_miglia(20), "miglia")


#----------------------------------------------------------------------------------------------------
#Esercizio su class methods

class Animale:
    
    numero_animali = 0 

#Inizializzazione del costruttore con incremento della variabile di classe ad ogni chiamata
    def __init__(self,nome,specie):
        
        Animale.numero_animali += 1
        self.nome = nome
        self.specie = specie

#classmethod che stampa il numero di animali
    @classmethod
    def quanti_animali(cls):
        print("Numero di animali creati", cls.numero_animali)
        

Animale_1 = Animale(" ", "Gatto")
Animale_2 = Animale("Hachiko", "Cane")
Animale_3 = Animale("Nuvola", "Coniglio")
Animale_4 = Animale("Nuvola", "Coniglio")


Animale.quanti_animali()
    
        