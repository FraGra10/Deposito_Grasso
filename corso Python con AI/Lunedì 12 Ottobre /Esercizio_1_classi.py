import math 

class Punto:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y 
        
    def muovi(self,dx,dy):
        
        self.x += dx 
        self.y += dy 
    
    def distanza_da_origine(self):
        
        return math.sqrt(self.x*self.x + self.y*self.y)
    
    
    
    
Punto_2 = Punto(1,0)
Punto_2.muovi(2,3)
print(Punto_2.distanza_da_origine())
    
    
#Esercizio 2 Classi 

class Libro: 
    
    def __init__(self,titolo,autore,pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
        
    
    def descrizione(self):
        
        return "Il libro", self.titolo, "è stato scritto dall'autore ", self.autore, "ed ha ", self.pagine, "pagine"
        


Lista_libri = []

while(True): 
    
    operazione= int((input("Vuoi inserire un libro o uscire? 1 o 2: ")))
    
    if(operazione == 1):
    
        titolo_libro = input("Inserisci il titolo del libro: ") 
        autore       = input("Inserisci l'autore del libro : ") 
        pagine       = int(input("Inserisci il numero di pagine del libro: "))     

        Libro_1 = Libro(titolo_libro,autore,pagine)
        Lista_libri.append(Libro_1)
        print(Libro_1.descrizione())
        

    else:
        break