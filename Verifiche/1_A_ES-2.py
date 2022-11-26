# Chiedi all'utente 2 numeri. 
# Se il primo è pari ed il secondo è dispari stampa "OPZIONE 1" altrimenti stampa "OPZIONE 2".  
n1 = int(input('Inserisci il primo numero: '))
n2 = int(input('Inserisci il secondo numero: '))
output = "OPZIONE 2"
if(n1 % 2 == 0):
    if(n2 % 2 != 0):
       output = "OPZIONE 1"
print(output)

# OPPURE
# if(n1 % 2 == 0):
#     if(n2 % 2 != 0):
#        print("OPZIONE 1")
#     else:
#         print("OPZIONE 2")
# else:
#     print("OPZIONE 2")