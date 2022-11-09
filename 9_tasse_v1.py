# ----- CONSEGNA ------ 
# Calcola le tasse da pagare e stampa il risultato.
# Se hai guadagnato meno di 10.000€ all'anno paghi 0€ di irpef. 
# Se hai guadagnato tra 10.000 e 30.000€ all'anno paghi il 22% di tasse. 
# Se hai guadagnato più di 30.000 euro paghi il 22% da 10.000 fino a 30.000 euro più il 33% della somma eccedente.
# Ad esempio se guadagno 36.000 euro allora pagherò 0€ per la parte da 0 a 10.000€,
# poi pagherò il 22% per la parte da 10.000€ a 30.000€ e
# paghero il 33% sulla parte eccedente i 30.000€ (ovvero 6000€).
# ---------------------

guadagno=int(input("inserisci guadagno:"))
tasse=0
if(guadagno<10000):
    tasse=0
else:
    if(guadagno<30000):
        tasse=22/100*guadagno
    else:
        tasse=22/100*20000
        tasse=tasse+33/100*(guadagno-30000)
print("devi pagare "+ str(tasse) + " € di tasse")

  
