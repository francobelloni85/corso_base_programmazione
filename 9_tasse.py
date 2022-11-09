# ----- CONSEGNA ------ 
# Calcola le tasse da pagare e stampa il risultato.
# Se hai guadagnato meno di 10.000€ all'anno paghi 0€ di irpef. 
# Se hai guadagnato tra 10.000 e 30.000€ all'anno paghi il 22% di tasse. 
# Se hai guadagnato più di 30.000 euro paghi il 22% da 10.000 fino a 30.000 euro più il 33% della somma eccedente.
# Ad esempio se guadagno 36.000 euro allora pagherò 0€ per la parte da 0 a 10.000€,
# poi pagherò il 22% per la parte da 10.000€ a 30.000€ e
# paghero il 33% sulla parte eccedente i 30.000€ (ovvero 6000€).
# ---------------------

tasse = 0
entrate = int(input('Quanto hai guadagnato quest\'anno?: '))

#Pago (se necessario) le tasse per il secondo scaglione
if (entrate > 10000):
    if(entrate >= 20000):
        tasse = (20000 - 10000) * 22 / 100
    else:
        tasse = (20000 - entrate) * 22 / 100

#Pago (se necessario) le tasse per il terzo scaglione
if (entrate > 30000):
    tasse_eccedenti_30000 = (30000 - entrate) * 33 / 100
    tasse = tasse + tasse_eccedenti_30000

print("Devi pagare " + str(tasse) + "€ di tasse!")
lettera = input("press any key to exit")