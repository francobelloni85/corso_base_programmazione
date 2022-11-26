# Chiedi all’utente 2 variabili. 
# Scambiare il contenuto delle due variabili se la prima variabile è minore della seconda
#  e la seconda variabile è pari. 
# Stampa il risultato indipendentemente dallo scambio
n1 = int(input('Inserisci il primo numero: '))
n2 = int(input('Inserisci il secondo numero: '))
if(n1 < n2):
    if(n2 % 2 == 0):
        t = n1
        n1 = n2
        n2 = t
print("n1 = " + str(n1))
print("n2 = " + str(n1))