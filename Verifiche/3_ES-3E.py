# Chiedi 3 numeri all'utente.
# Questi numeri sono compresi tra 1 e 90. Questi 3 numeri sono diversi tra loro.
# Continua a chiedere i 3 numeri se l’utente inserisce dei dati errati.
# Stampa tutti i numeri che sono presenti tra il numero minore e il numero maggiore inseriti.
# Invece di stampare il numero centrale dei tre numeri inserito stampa la stringa “Numero Utente”.

# Esempio di esecuzione.
# “Numero uno?” 7
# “Numero due?” 2
# “Numero tre?” 4
# Risultato:
# 2
# 3
# Numero Utente
# 5
# 6
# 7

# SUGGERIMENTO:
# DIVIDERE IL PROBLEMA GRANDE IN PICCOLI PROBLEMI RISOLVIBILI FACILMENTE

while True:
    n1 = int(input("n1: "))
    n2 = int(input("n2: "))
    n3 = int(input("n3: "))
    # Controlli per il n1
    if( n1 <= 0 ): continue
    if( n1 > 90 ): continue
    # Controlli per il n2
    if( n2 <= 0 ): continue
    if( n2 > 90 ): continue
    # Controlli per il n3
    if( n3 <= 0 ): continue
    if( n3 > 90 ): continue
    # Numeri diversi tra loro
    if (n1 == n2): continue
    if (n2 == n3): continue
    if (n1 == n3): continue
    print("numeri ok")
    break


max = 0
medio = 0
min = 0

# 1-OPZIONE n1 è il maggiore
if(n1 > n2):
    if(n1 > n3):
        max = n1
        if(n2 > n3):
            medio = n2    
            min = n3
        else:
            min = n2    
            medio = n3

# 2-OPZIONE n2 è il maggiore
if(n2 > n1):
    if(n2 > n3):
        max = n2
        if(n1 > n3):
            medio = n1    
            min = n3
        else:
            min = n1    
            medio = n3

# 3-OPZIONE n3 è il maggiore
if(n3 > n1):
    if(n3 > n2):
        max = n3
        if(n2 > n1):
            medio = n2 
            min = n1
        else:
            min = n3    
            medio = n2

print("Max", max)
print("Medio", medio)
print("Min", min)

# STAMPA
i = min
while i < max:
    if (i != medio):
        print(i)
    else:
        print("Numero utente")
    i = i + 1


# METODO VERBOSO:
# 
# # MAX -----------------------
# 
# # Controllo che il max sia n1
# if (n1 > n2):
#     if (n1 > n3):
#         max = n1
# 
# # Controllo che il max sia n2
# if (n2 > n1):
#     if (n2 > n3):
#         max = n2
# 
# # Controllo che il max sia n3
# if (n3 > n1):
#     if (n3 > n2):
#         max = n3
# 
# # MIN -----------------------
# 
# # Controllo che il max sia n1
# if (n1 < n2):
#     if (n1 < n3):
#         min = n1
# 
# # Controllo che il max sia n2
# if (n2 < n1):
#     if (n2 < n3):
#         min = n2
# 
# # Controllo che il max sia n3
# if (n3 < n1):
#     if (n3 < n2):
#         min = n3
# 
# print("Max", max)
# print("Min", min)
# 
# # CALCOLO NUEERO MEDIO
# 
# # numero medio
# if (n1 == max or n1 == min):
#     if(n3 == max or n2 == min):
#         medio = n2
# 
# if (n2 == max or n2 == min):
#     if(n3 == max or n2 == min):
#         medio = n1
# 
# if (n2 == max or n2 == min):
#     if(n1 == max or n1 == min):
#         medio = n3