# ----- CONSEGNA ------ 
# Chiede all'utente il lato di un quadrato. 
# Si calcola l'area e il perimetro. Poi si stampano i risultati.
# ---------------------

# salvo nella variabile "latoquadrato_stringa" il valore inserito dall'utente
latoquadrato_stringa = input('Inserisci il lato del quadrato: ')

# converto in numero il valore della variabile latoquadrato_stringa
latoquadrato = int(latoquadrato_stringa)

# calcolo il perimetro e lo salvo nella variabile
perimetro = latoquadrato *4

# calcolo l'area e la salvo nella variabile
area = latoquadrato * latoquadrato

# stampo i risultati
print('Il risultato del perimetro è: ',perimetro)
print('Il risultato del area è: ', area)

# exit 
x = input('type any letter to exit ...')