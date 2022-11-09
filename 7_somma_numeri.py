# ----- CONSEGNA ------ 
# Chiedi 3 numeri all'utente. 
# Se la somma è maggiore di 10 scrivi il numero maggiore dei tre.
# Altrimenti stampa la somma dei tre numeri. 
# ---------------------
s = 0
n1 = int(input('Inserisci il primo numero: '))
n2 = int(input('Inserisci il secondo numero: '))
n3 = int(input('Inserisci il terzo numero: '))
max = 0

s = n1 + n2 + n3

if(s > 10):
    # trovo il maggiore se è n1
    if(n1 >= n2):
        if(n1 >= n3):
            max = n1

    # trovo il maggiore se è n2
    if(n2 >= n1):
        if(n2 >= n3):
            max = n2
    
    # trovo il maggiore se è n3
    if(n3 >= n1):
        if(n3 >= n2):
            max = n3

    print(max)
    
else:
    print(s)

lettera = input("press any key to exit")