#Qui proveremo le variabili e i tipi di variabili 


#Esempio di accesso ai caratteri delle variabili

nomeVariabile = "valore"

numero = 1

print(nomeVariabile[0])
print(nomeVariabile[2])


#Concatenazione delle stringhe
saluto = "Ciao"
nome = "Francesco"
messaggio = saluto + " " + nome

print(messaggio)

#Esempio sui metodi delle stringhe 

stringa = "Oggi, è 5 Ottobre"
print(len(stringa))
print(stringa.upper())
print(stringa.split(','))
print(stringa.replace('Ottobre','Novembre'))

#Esempi sui Booleani
bool_t = True
bool_f = False 

x= 12
y = 10

print(x == y)
print(x != y)
print(x < y)

#Esempi sull'uso di and,or e not
x = 5
y= 7
z=25

print(x < y and z > y)
print(not z < x)
print(x > y or y > z)