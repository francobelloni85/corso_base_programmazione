# Chiedi 3 numeri all'utente.
# Questi numeri sono compresi tra 0 e 100. I numeri inseriti dall’utente sono 2 pari e 1 dispari. 
# Continua a chiedere i 3 numeri se l’utente inserisce dei dati errati. 
# Stampa tutti i numeri che sono presenti tra 0 e il primo numero inserito
# prestando però attenzione di stampare la stringa “Numero Utente” 
# se il terzo o secondo numero inserito dall’utente sono compresi nella fase di stampa.

# Esempio di esecuzione.
# “Numero uno?” 7
# “Numero due?” 2
# “Numero tre?” 4
# Risultato:
# 0
# 1
# Numero Utente
# 3
# Numero Utente
# 5
# 6
# 7

# SUGGERIMENTO:
# DIVIDERE IL PROBLEMA GRANDE IN PICCOLI PROBLEMI RISOLVIBILI FACILMENTE

conta_pari: int = 0
conta_dispari: int = 0

while True:
    n1 = int(input("n1: "))
    n2 = int(input("n2: "))
    n3 = int(input("n3: "))
    # Controlli per il n1
    if( n1 < 0 ): continue
    if( n1 > 100): continue
    # Controlli per il n2
    if( n2 < 0 ): continue
    if( n2 > 100): continue
    # Controlli per il n3
    if( n3 < 0 ): continue
    if( n3 > 100 ): continue
    
    # Controllo se pari o dispari per n1
    if (n1 % 2 == 0) :
        conta_pari = conta_pari + 1
    else:
        conta_dispari = conta_dispari + 1

    # Controllo se pari o dispari per n2
    if (n2 % 2 == 0) :
        conta_pari = conta_pari + 1
    else:
        conta_dispari = conta_dispari + 1
    
    # Controllo se pari o dispari per n3
    if (n3 % 2 == 0) :
        conta_pari = conta_pari + 1
    else:
        conta_dispari = conta_dispari + 1
    
    if(conta_pari == 2):
        if (conta_dispari == 1):
            break

i: int = 0
while i <= n1:    
    output = i
    if(i == n2):
        output = "Numero utente"
    if(i == n3):
        output = "Numero utente"
        
    print (output)
    i = i + 1

print ("fine")