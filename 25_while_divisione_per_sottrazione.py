# VARIABILI
i = 0
dividendo = 0
divisore = 0
# dividendo_originale = 0

# PRIMO CICLO WHILE
# Chiedo i numeri
while True:
    dividendo = int(input("Inserisci dividendo: "))
    divisore = int(input("Inserisci divisore: "))
    if(dividendo >= 0):
        if(divisore > 0):
            break

# dividendo_originale = dividendo

# Calcolo la divisione
while True:
    dividendo = dividendo - divisore
    if (dividendo > 0):
        i = i + 1
    else:
        break

# resto = dividendo_originale - (i * divisore)
resto = dividendo + divisore
print("Il risultato della divisione è: " + str(i))
print("Il resto della divisione è: " + str(resto))
