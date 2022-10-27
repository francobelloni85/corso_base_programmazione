# ----- CONSEGNA ------ 
# Stampa alla fine del programma
# il numero massimo e il numero minimo di tutti i numeri che l'utente ha inserito. 
# Si esce dal ciclo quando l'utente inserisce il numero 0.
# Versione piu' prolissa
# ---------------------

message: str = 'Inserisci un numero: '
number: int = int(input(message))

# Salvo direttamente il primo valore,
# inizializzando le variabili
max = number
min = number
count = 0

while True:    

    if (count != 0):
        number: int = int(input(message))  
    
    # Esco dal ciclo se ho inserito il numero 0
    if (number == 0):
        break

    # Controllo se c'è un nuovo numero massino, se si lo salvo
    if (number > max):
        max = number

    # Controllo se c'è un nuovo numero minimo, se si lo salvo
    if (number < min):
        min = number

    count = count + 1

print("Max: ", max)
print("Min: ", min)

a=input("Press any key to exit")