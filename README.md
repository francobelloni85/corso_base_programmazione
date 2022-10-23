# Corso base di programmazione

Programmi in python in ordine crescente di difficolta'.

------------

## CODICE UTILE

esempi BREVI di codice python / parole chiave del linguaggio:

> Chiede all'utente di inserire un numero, questo valore è salvato nella variabile latoquadrato_stringa

`latoquadrato_stringa = input('Inserisci il lato del quadrato: ')`

.

> Il valore inserito viene convertito in un numero

`latoquadrato = int(latoquadrato_stringa)`

.

> Stampo a schermo una stringa insieme al valore della variabile perimetro

`print('Il risultato del perimetro è: ',perimetro)`

## Sintassi IF/ELSE

> Se la variabile A è uguale alla variabile B

`if(A == B):`

`_____print("Numeri uguali")"`

`else:`

`_____print("Numeri uguali")"`

### Sintassi WHILE

> Entro nel ciclo fino a che la variabile i è minore di 6

`while i < 6:`

> Esco dal ciclo se i è uguale a 3 senza aspettare la fine

`while i < 6:`

`if i == 3:`

`____break`

> è simile ad un goto, si torna direttamente all'istruzione while i < 6:

`while i < 6:`

`if i == 3:`

`____continue`

------------

## ESERCIZI

### IF-ELSE

**(1_hello_world.py)** Stampa la stringa "Ciao Mondo" per controllare di aver installato correttamente python sul proprio pc.

**(2_lato_quadrato.py)** Chiede all'utente il lato di un quadrato. Si calcola l'area e il perimetro. Poi si stampano i risultati.

**(3_stampa_nomi.py)** Ci sono 5 nomi: Alina, Bruno, Carlo, Dario, Emilio. Chiedi una lettera all'utente. Stampa il nome corrispondente alla prima lettera. Se non è nella lista stampa "you chose ... poorly".

**(4_if_numeri.py)** Chiedi 2 numeri all'utente. Se il primo è maggiore di 10 scrivi "FUORI SCALA". Se il secondo numero è maggiore di 50 scrivi "TROPPO GRANDE". Se non hai stampato nulla allora stampa "TUTTO OK"

**(5_numero_pari.py)**  Chiedi all'utente un numero pari. Se il numero inserito è pari somma il numero inserito al numero 3 e restituisci il risultato. Se è dispari stampa la frase "hai inserito un numero dispari birbante!"

**(7_somma_numeri.py)**  Chiedi all'utente di inserire 3 numeri. Se la somma è maggiore di 10 allora restituisci il numero più grande. Se invece non è maggiore di 10 restituisci la somma dei 3 numeri.

**(8_calcolatrice.py)**  Chiedi all'utente 2 numeri. Poi chiedi un numero per l'operazione da effettuare tra somma (1), sottrazione (2), divisione (3), moltiplicazione (4). Stampa il risultato. Presta attenzione per la divisione per zero e stampa il messaggio di errore "Non puoi dividere per zero!".
Se l'utente sceglie un operazione non contemplata effettua la somma.

**(9_tasse.py)**  Calcola le tasse da pagare e stampa il risultato. Se hai guadagnato meno di 10.000€ all'anno paghi 0€ di irpef. Se hai guadagnato tra 10.000 e 30.000€ all'anno paghi il 22% di tasse. Se hai guadagnato più di 30.000 euro paghi il 22% da 10.000 fino a 30.000 euro più il 33% della somma eccedente.

------------

### WHILE

**(10_stampa_while.py)**  Stampa i primi 10 numeri con il cliclo while.

**(11_numero_magico.py)**  Chiedi all'utente di indovinare un numero magico.Il numero magico è il numero 7. L'utente ha 10 tentativi.Se indovina stampa "Complimenti, hai indovinato!" Se non indovina stampa "Game over!" alla fine dei 10 tentativi

**(12_stampa_while_pari.py)**  Stampa i primi 10 numeri con il cliclo while. Se sono pari stampa anche un punto escamativo vicino al numero. 1 - 2! - 3 - 4!

**(13_stampa_while_pattern.py)**  Stampa il seguente pattern:

1

1 2 

1 2 3 

1 2 3 4 

1 2 3 4 5

**(14_somma_while.py)**  Chiedi un numero all'utente e somma i numeri da 1 fino al numero immesso.

**(15_media_while.py)**  Calcola la media di tutti i numeri che l'utente ha inserito fino a quel momento. Quando l'utente inserisce il numero 0 allora stampa il risultato.

**(16_max_min_while.py)**  Stampa alla fine del programma il numero massimo e il numero minimo di tutti i numeri che l'utente ha inserito. Si esce dal ciclo quando l'utente inserisce il numero 0.

**(17_while_calcolatrice.py)**  Chiedi all'utente quante operazioni vuole fare con la calcolatrice. Poi chiedi 2 numeri. Infine chiedi un numero per l'operazione da effettuare tra somma (1), sottrazione (2), divisione (3), moltiplicazione (4). Alla fine delle operazioni stampa il risultato. Presta attenzione per la divisione per zero e stampa il messaggio di errore "Non puoi dividere per zero!" ed esci dal programma nel caso. Se l'utente sceglie un operazione non contemplata effettua la somma.

**(18_numeri_primi_while.py)**  Chiedi un numero all'utente e trova tutti i numeri primi fino al numero immesso

------------

## PROGETTI

**(A_morra_cinese.py)**  Crea il gioco "Carta-Sasso-Forbici" da giocare contro il computer. Il computer gioca sempre CARTA, poi SASSO e infine FORBICI. Il gioco finisce quando l'utente o il pc vincono 2 parite.
Inizialmente si chiede all'utente cosa vuole giocare, poi si confronta con il risultato del pc. Ad ogni mano si informa se c'è stato un pareggio, una vittoria oppure una sconfitta. Viene anche mostrato il riepilogo del risultato del gioco con tutte le mani disputate: VITTORIE=..., SCONFITTE =..., PAREGGI=...
