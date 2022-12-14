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

### Sintassi RANDOM

Per poter generare un numero random bisogna usare una funzione di python. Nel concreto bisogna:

1) Scrivere `import random` all'inizio del file

2) Usare la funzione random.randrange() che ci permette di ottenere un numero random

Le 2 funzioni che usiamo sono:

`n = random.randrange(100)`

`m = random.randrange(50,100)`

n sarà un numero compreso tra 0 e 100. m sarà un numero compreso tra 50 e 100.

## TABELLA VALUTAZIONE PROGETTO

Nel secondo quadrimestre bisognerà pensare, programmare e presentare 3 programmi.

Il voto sarà così composto:

| Valutazione        | Punti |
| ------------------ | ----- |
| Documentazione     | 2     |
| Logica/Difficolta  | 3     |
| Codice             | 2     |
| Esposizione        | 2     |
| Git                | 1     |

Una volta concluso il progetto bisognerà creare una presentazione di massimo 20 min in cui si espongono le parti salienti.

Il progetto per poter avere tutti e 3 i punti di "Logica/Difficolta" dovrà essere abbastanza corposo e prevedere una qualche specie di algoritmo e decisione sulle variabili.

Per la documentazione si può seguire il progetto di prova che si trova nella cartella PROGETTI. La documentazione deve includere una analisi dei requisiti, ...

Una volta deciso il proprio progetto si scrive un messaggio (con una descrizione approfondita) nel gruppo TEAMS dove risponderò con APPROVATO/NON APPROVATO.

## LINK UTILI

[Stringhe](https://www.pythoncollege.it/tutorial/stringhe-in-python/)

[Liste](https://www.pythoncollege.it/tutorial/liste-in-python/)

[Funzioni](https://www.pythoncollege.it/tutorial/funzioni-in-python/)

------------

## ESERCIZI

### IF-ELSE

**(1_hello_world.py)** Stampa la stringa "Ciao Mondo" per controllare di aver installato correttamente python sul proprio pc.

**(2_lato_quadrato.py)** Chiede all'utente il lato di un quadrato. Si calcola l'area e il perimetro. Poi si stampano i risultati.

**(3_stampa_nomi.py)** Ci sono 5 nomi: Alina, Bruno, Carlo, Dario, Emilio. Chiedi una lettera all'utente. Stampa il nome corrispondente alla prima lettera. Se non è nella lista stampa "you chose ... poorly".

**(4_if_numeri.py)** Chiedi 2 numeri all'utente. Se il primo è maggiore di 10 scrivi "FUORI SCALA". Se il secondo numero è maggiore di 50 scrivi "TROPPO GRANDE". Se non hai stampato nulla allora stampa "TUTTO OK"

**(5_numero_pari.py)**  Chiedi all'utente un numero pari. Se il numero inserito è pari somma il numero inserito al numero 3 e restituisci il risultato. Se è dispari stampa la frase "hai inserito un numero dispari birbante!"

**(6_ordine_crescente.py)**  Visualizza in ordine crescente 3 numeri inseriti dall'utente.

**(7_somma_numeri.py)**  Chiedi all'utente di inserire 3 numeri. Se la somma è maggiore di 10 allora restituisci il numero più grande. Se invece non è maggiore di 10 restituisci la somma dei 3 numeri.

**(8_calcolatrice.py)**  Chiedi all'utente 2 numeri. Poi chiedi un numero per l'operazione da effettuare tra somma (1), sottrazione (2), divisione (3), moltiplicazione (4). Stampa il risultato. Presta attenzione per la divisione per zero e stampa il messaggio di errore "Non puoi dividere per zero!".
Se l'utente sceglie un operazione non contemplata effettua la somma.

**(9_tasse.py)**  Calcola le tasse da pagare e stampa il risultato. Se hai guadagnato meno di 10.000€ all'anno paghi 0€ di irpef. Se hai guadagnato tra 10.000 e 30.000€ all'anno paghi il 22% di tasse. Se hai guadagnato più di 30.000 euro paghi il 22% da 10.000 fino a 30.000 euro più il 33% della somma eccedente. Ad esempio se guadagno 36.000 euro allora pagherò 0€ per la parte da 0 a 10.000€, poi pagherò il 22% per la parte da 10.000€ a 30.000€ e paghero il 33% sulla parte eccedente i 30.000€ (ovvero 6000€).

**(10A_date.py)**  Ricevute in input due date (giorno-mese-anno) determinare la piu piccola.

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

**(17_while_calcolatrice.py)**  Chiedi all'utente quante operazioni vuole fare con la calcolatrice. Successivamente chiederi 2 numeri e l'operazione da effettuare. l'operazione da effettuare è tra somma (1), sottrazione (2), divisione (3), moltiplicazione (4). Se l'utente vuole effettuare più di una operazione allora al risulto ottenuto applica l'operazione scelta di volta in volta immessa dall'utente.
Alla fine delle operazioni stampa il risultato. Presta attenzione per la divisione per zero e stampa il messaggio di errore "Non puoi dividere per zero!" ed esci dal programma nel caso. Se l'utente sceglie un operazione non contemplata effettua la somma.
Esempio di esecuzione:

"scegli quante operazioni fare: " 3, "Inserisci il primo numero: " 5, "Inserisci il secondo numero: " 3, abbiamo che risulto = 8. Ora viene chiesto all'utente una delle altre 2 operazioni rimanenti. "Inserisci un numero", 8. Poi viene chiesto "Inserisci l'operazione: ", in questo caso sottrazione. Il risultato ora è 0. Poi si prosegue con il resto delle operazioni rimaste.

**(18_numeri_primi_while.py)**  Chiedi un numero all'utente e trova tutti i numeri primi fino al numero immesso.

**(19_classifica_squadre.py)** Chiedi all'utente il nome di 3 squadre di calcio. Per ogni squadra inserisci quante partite la squadra ha vinto, pareggiato o perso. Infine stampa la classifica generale. [VERY HARD!]

**(20_doppio_o_meta.py)**  In questo programma continua a chiedere dei numeri all'utente. Se il numero immesso è pari moltiplica il primo numero immesso dall'utente per 2. Se è dispari dividi per 2 il primo numero immesso dall'utente. Moltiplica o dividi per 2 per i numeri successivi al primo con la stessa logica usando il risultato ottenuto nella prima operazione. Esci dal ciclo e stampa il risultato quando l'utente inserisce il numero 0.

**(21_while_pari_dispari.py)**  In questo programma continua a chiedere dei numeri all'utente. Se il numero immesso è pari stampa pari. Se è dispari stampa dispari. Esci dal ciclo se l'utente inserisce un numero che è doppio rispetto all'ultimo numero immesso. Es. Inserisco 2 poi inserisco 4 al ciclo successivo devo quindi uscire.

**(22_while_concatena_stringa.py)**
Chiedi 10 numeri all'utente. Conta quante volte il numero è maggiore di 50. Conta quante volte il numero minore di 15.
Alla fine stampa una stringa in base al conteggio. Nella stringa ci saranno tanti * quanti sono i numeri maggiori di 50 e # quanti sono i numeri minori di 15. Esempio: 80,4,22,100,150,5,43,65,2,45 ovvero 4 numeri>50 e 3 numeri < 15. La stringa finale sarà: ****###.

**(23_while_conta_successivo.py)**  Chiedi 10 numeri all'utente. Stampa quante volte il numero appena inserito è maggiore del numero precedente. Ad esempio con 5 numeri: 10 11 9 3 5 il risultato è 2.

**(24_while_conta_successivo_doppio.py)**  Chiedi 10 numeri all'utente. Stampa quante volte il numero appena inserito è maggiore sia del numero precedente sia del numero precedente al precedente. Ad esempio con 5 numeri: 10 11 15 3 5 il risultato è 1.

**(25_while_divisione_per_sottrazione.py)**  Chiedi 2 numeri positivi all'utente. Ripeti l'operazione se uno dei due è negativo o 0. Questi 2 numeri sono chiamati divisore e dividento. Stampa il risultato della divisione applicando il metodo delle divisioni successive.
Es. Divisore 13 e dividento = 5. Risultato = 2 con resto = 3

**(26_numero_segreto_v2.py)**  Chiedi all'utente di indovinare un numero segreto. Se il numero immesso diverso da quello da indovinare dai all'utente un piccolo indizio formato dalla stringa ("Piu' piccolo/grande") e dall'aggettivo "acqua, fuochino, fuoco" in base alla differenza tra i 2 numeri.

differenza >= 20        -> acqua

10 > differenza < 20    -> fuochino

differenza < 10         -> fuoco

Es. numero più grande - fuoco

Una volta indovinato il numero stampa il numero di tentativi che sono stati necessari per indovinare.

**(27_fattori.py)**  Chiedi 1 numero positivo all'utente. Ripeti l'operazione se il numero è zero oppure negativo. Stampa i fattori del numero.
X è un fattore del numero N se il resto della divisione tra N ed X è uguale a zero. Il fattori di 10 sono 1,2,5,10.

**(28_numero_primo.py)**  Stampa se il numero immesso è un numero primo.

**(29_random.py)**  Genera un numero random. Stampa se pari o dispari.

**(30_calcola_frequenze.py)**  Calcola e stampa le frequenze di 100 lanci di dadi. (es. numero 1 uscito 33 volte, numero 2 uscito 21 volte, ...)

**(31_calcola_pagella.py)**  Chiedi all'utente di inserire 2 voti per materia. Le materie sono 5 Matematica, Italiano, Storia, Inglese e Informatica. Calcola se l'utente è promosso oppure bocciato. Si è promossi se la media è superiore a 6 ed è presente solamente una materia insufficente.

------------

## AND OR NOT

**(50_data.py)**  Chiedi 3 numeri all'utente come se fossero una data. (Giorno, Mese, Anno). Stampa la data se è corretta oppure tanti messaggi di errore, uno per ogni inesattezza. ES 50 12 1985 => "Un mese al massimo ha solo 31 giorni". Presta attenzione a Febbraio e anni bisistili!

**(51_lotto.py)**  Gioco del lotto. Chiedi all'utente 5 numeri. I numeri da indovinare sono = 6, 12, 18, 3, 5. Stampa "Ambo", "tris", "quaterna", "cinquina" nel caso l'utente indovini. Controlla solo se l'utente non iserisca numeri > 90.

**(52_lotto_hard.py)**  Gioco del lotto. Chiedi all'utente 5 numeri. I numeri da indovinare sono = 6, 12, 18, 3, 5. Stampa "Ambo", "tris", "quaterna", "cinquina" nel caso l'utente indovini. Controlla che l'utente non iserisca numeri > 90 e un numero già immesso.

------------

### STRINGHE

**(101_stringa_libro.py)**  Stampare una stringa (che sia l'inizio di un libro) in verticale.

**(102_conta_vocali.py)**  Chiedere una stringa all'utente e contare il numero di vocali.

**(103_numeri_in_stringa.py)**  Chiedere una stringa di sole cifre all'utente. Controlla che sia vero. Se si somma il valore dei numeri presenti. Se no chiedi ancora la stringa.

------------

## PROGETTI

**(A_morra_cinese.py)**  Crea il gioco "Carta-Sasso-Forbici" da giocare contro il computer. Il computer gioca sempre CARTA, poi SASSO e infine FORBICI. Il gioco finisce quando l'utente o il pc vincono 2 parite.
Inizialmente si chiede all'utente cosa vuole giocare, poi si confronta con il risultato del pc. Ad ogni mano si informa se c'è stato un pareggio, una vittoria oppure una sconfitta. Viene anche mostrato il riepilogo del risultato del gioco con tutte le mani disputate: VITTORIE=..., SCONFITTE =..., PAREGGI=...

**(D_crea_squadre_random.py)**  Crea un programma che permetta di creare n squadre di alunni in modo random. Gli input sono il numero di alunni della classe e il numero di squadre.

N alunni = 20

N squadre = 4

L'output deve essere:

Squadra1 = 2,6,7,10,12

Squadra2 = 1,11,9,15,19

Squadra3 = 4,5,8,14,18

Squadra4 = 18,17,16,20,3

I numeri del registro non si devono ripetere.

------------

## LINK PROGETTI STUDENTI

<https://isiskeynes-my.sharepoint.com/:x:/g/personal/francesco_belloni_isiskeynes_it/EXpPcFgU5FpEnlMrroA0-n4BSscG1DhI4ZgiElP4k7HGWg?e=k0YOsA>
