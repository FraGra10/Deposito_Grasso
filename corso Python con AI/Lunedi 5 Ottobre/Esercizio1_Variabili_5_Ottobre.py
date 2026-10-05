#Creo una variabile per ogni tipo di dato basilare

x = int(input("Inserisci un intero: "))
y = float(input("Inserisci un numero in virgola mobile: "))
stringa = input("Inserisci la stringa: ")
carattere = input("Inserisci il carattere: ")
flag = bool(input("Inserisci il valore booleano: "))

#Stampo tutte le variabili in un unico print

print(stringa, " il valore di x è: ", x, " il valore di y è: ", y , " il primo carattere della stringa è: ", carattere , "La flag è: ", flag)

#Operatori logici e di confronto 

primo_numero = int(input("Inserisci primo numero:"))
secondo_numero = int(input("Inserisci secondo numero:"))

print(primo_numero > secondo_numero)
print(primo_numero < secondo_numero)
print(primo_numero == secondo_numero)
print(primo_numero > secondo_numero or secondo_numero < primo_numero)
print(primo_numero > secondo_numero and secondo_numero < primo_numero)
print(not( primo_numero > 0))