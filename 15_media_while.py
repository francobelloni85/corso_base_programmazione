# ----- CONSEGNA ------ 
# Calcola la media di tutti i numeri che l'utente ha inserito fino a quel momento.
# Quando l'utente inserisce il numero 0 allora stampa il risultato.
# ---------------------

# Valore che inserisce l'utente
numero = 0 
# Tengo conto del totale
totale = 0
# Conta quante volte ho immesso un numero
i = 0

# Entro nel ciclo.
while True :
    # Mi salvo nella variabile il numero inserito dall'utente
    numero = int(input('Inserisci un numero: '))
    # Posso uscire dal ciclo solamente se inserisco lo 0 come numero
    if (numero == 0):
        break
    # Mi calcolo il totale
    totale = totale + numero    
    # Aumento il contatore dei numeri inseriti
    i = i + 1 

# Mi calcolo la media
media = totale/i

print("Hai inserito " + str(i)+ " numeri.")
print("Il totale è: " + str(totale))
print("La media è: " + str(media))

a=input("Press any key to exit")