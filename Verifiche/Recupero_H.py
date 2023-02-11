# ----- CONSEGNA ------ 
# Chiedi all'utente due numeri.
# Trasforma quelli dispari in pari aggiungendo 1.
# Dividi tutti i numeri per 2. 
# Se la somma dei due numeri divisi è minore di 100 richiedi nuovamente i due numeri. 
# Infine, stampa in due numeri in ordine decrescente. 
# ---------------------

number_1 : int = 0
number_2 : int = 0

message: str = "Inserisci un numero: "
error_message_1: str = "La somma non rispetta i requisiti"

while(True):
    number_1 = int(input(message))
    number_2 = int(input(message))

    # Trasformo tutti i numeri dispari in pari
    number_1 = (number_1 + (number_1 % 2)) / 2
    number_2 = (number_2 + (number_2 % 2)) / 2

    # Check per uscire dal ciclo
    if((number_1 + number_2) < 100):
        print(error_message_1)
    else:
        break    

# Stampo in ordine decrescente
result: list = [number_1,number_2]
result.sort(reverse=True)
print(result)



