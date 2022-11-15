# Chiedi 10 numeri all'utente. 
# Stampa quante volte il numero appena inserito è maggiore del numero precedente. 
# Ad esempio con 5 numeri: 10 11 9 3 5 il risultato è 2

numero_inserito = int(input("Inserisci un numero: "))
numero_precedente = numero_inserito
numeri_maggiori = 0
i = 1

while i <= 9:
    # Chiedo il numero all'utente
    numero_inserito=int(input("Inserisci un numero: "))
    # Se il nuovo numero è maggiore del precedente allora 
    # devo incrementare il contatore
    if(numero_inserito > numero_precedente):
        numeri_maggiori=numeri_maggiori+1

    # sovrascrivo la variabile, salvando il 
    # "vecchio numero"
    numero_precedente = numero_inserito
    
    # aumento il contatore
    i=i+1

print(numeri_maggiori)

