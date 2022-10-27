# ----- CONSEGNA ------ 
# Stampa alla fine del programma
# il numero massimo e il numero minimo di tutti i numeri che l'utente ha inserito. 
# Si esce dal ciclo quando l'utente inserisce il numero 0.
# ---------------------

message: str = 'Inserisci un numero: '
number: int = int(input(message))
# Salvo direttamente il primo valore,
# inizializzando le variabili
max = number
min = number

while number != 0:  
    # Controllo se c'è un nuovo numero massino, se si lo salvo
    if (number > max):
        max = number
    # Controllo se c'è un nuovo numero minimo, se si lo salvo
    if (number < min):
        min = number
    # Chiedo il prossimo numero
    number: int = int(input(message)) 

print("Max: ", max)
print("Min: ", min)

a=input("Press any key to exit")