# ----- CONSEGNA ------ 
# Chiedi 3 numeri dispari all'utente. 
# Se viene inserito un numero pari stampa "Inserisci solo numeri dispari" e chiedi nuovamente i numeri.  
# Se sono tutti e 3 dispari esegui la somma dei 3 numeri e se è compresa tra 20 e 40 stampa "Fine" e il risultato.
# Se no richiedi nuovamente i 3 numeri. 
# ---------------------

number_1 : int = 0
number_2 : int = 0
number_3 : int = 0
somma: int = 0

message: str = "Inserisci un numero dispari: "
error_message_1: str = "Inserisci solo numeri dispari!"
error_message_2: str = "La somma non rispetta i requisiti"

while(True):
    number_1 = int(input(message))
    number_2 = int(input(message))
    number_3 = int(input(message))
    
    # Validazione degli input
    if((number_1 % 2 == 0) or (number_2 % 2 == 0) or (number_3 % 2 == 0)):
        print(error_message_1)
        continue
    
    # Parte di "logica"
    somma = number_1 + number_2 + number_3
    if (20 <= somma <= 40):
        break
    print(error_message_2)

print("Fine")
print(somma)



