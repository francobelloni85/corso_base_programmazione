# ----- CONSEGNA ------ 
# 1)	Continua a chiedere 2 numeri positivi all’utente. I 2 numeri sono il numero da convertire e il numero di bit.
# 2)	Stampa la conversione del numero (non importa il senso di lettura)
# 3)	Se il numero immesso supera il numero di bit necessari per contenerlo stampa la scritta “Errore overflow” e non effettuare la conversione
# 2^n – 1 è la formula per il controllo della dimesione dei bit necessari per contenere il numero.
# ---------------------

n = int(input("inserisci il numero da convertire: "))
n_bit = int(input("inserisci il numero di bit: "))

# Contatore
i = 0
# Mi conta il numero massimo che posso gestire
conteggio_bit = 1 

while(i < n_bit):
    conteggio_bit= conteggio_bit * 2
    i = i + 1

if(n > conteggio_bit):
    print("Errore over flow")
    print("Puoi arrivare al max a : " + str(conteggio_bit))
else:
    while(n != 0):
        # Controllo il resto della divisione
        if(n % 2 == 0):
            print("0")
        else:
            print("1")
        n = int(n / 2)
