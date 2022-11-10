# ----- CONSEGNA ------ 
# In questo programma continua a chiedere dei numeri all'utente.
# Se il numero immesso è pari stampa pari. Se è dispari stampa dispari.
# Esci dal ciclo se l'utente inserisce un numero che è doppio rispetto all'ultimo numero immesso. Es. 
# Inserisco 2 poi inserisco 4 al ciclo successivo devo quindi uscire.
# ---------------------
numero=0
ultimo_numero=0 
i=1
while True:
    numero=int(input('Inserisci il numero: '))
    # devo avere 2 numeri per poter effettuare il confronto
    # se ne ho solo 1 allora "ritorno" al while true
    if (i == 1):
        i = 2
        continue

    if (numero % 2 == 0):
        print ('Pari')
    else:
        print('Dispari')
    
    if (numero == ultimo_numero * 2):
        break
    else:
        ultimo_numero=numero

print('Fine')