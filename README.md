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

### Sintassi STRINGHE

La stringa è un dato immutabile. Una volta inizializzata non è più possibile modificarla. Si può solamente sostituire il suo valore.

Inizializzo una stringa con un valore

`text: str = "Hello word"`

Accedo al singolo carattere con la sintassi delle parentesi quadrate

`i: int = 0`

`singolo_carattere: str = text[i]`

singolo_carattere vale 'H' ovvero il primo carattere della stringa. Se aumento l'indice i:

`i = i + 1`

`singolo_carattere = text[i]`

singolo_carattere ora vale 'e' ovvero il secondo carattere della stringa.

Per concatenare due strighe si usa il simbolo +:

`prima: str = "Hello"`

`seconda: str = " word"`

`totale: str = prima + seconda`

nella variabile totale si avrà il valore "Hello word".

Per convertire una stringa in numero si usa la funzione `int()` se si tratta di un intero.

`i: int = int("5")`

la variabile i ora ha il valore numerico 5.

Per poter stampare un numero insime una stringa bisogna usare la funzione `str`. str trasforma il numero in stringa. Ad esempio:

`print("è uscito il numero: " + str(i) + " sulla ruota di Bari.")`

Per trasformare in maiuscolo e minuscolo si possono usare le funzioni `lower()` e `upper()`:

`string_a = 'iLovePython'`

`string_b = 'iLovePython'`

il risultato con:

`print(string_a.lower())`

`print(string_b.upper())`

sara "ilovepython" tutto in minuscolo e "ILOVEPYTHON" tutto in maiuscolo.

### CONVERSIONI E OPERATORI

Se eseguimo `a = 24 / 10`

il risultato a sarà 2.4 un numero in virgola mobile.

se vogliamo la parte intera del risultato dobbiamo utilizzare il comando `int()`:

`b = int(24 / 10)`

b in questo caso è 2.

Se vogliamo il resto della divisione dobbiamo usare l'operatore `%`. il simbolo `%` ci permette di ottere il resto della divisione.

`c = int(24 % 10)`

c in questo caso avrà il valore 4.

le conversioni che si possono effettuare sono:

int(x), str(x), float(x), bool(x)

### INDICAZIONI FLOW CHAR

Quando andiamo ad disegnare il flowchar dell'esercizio bisogna indicare:

- il tipo di dato (int, string, double, bool, char) per ogni variabile.

- indicare se il dato è una variabile oppure è una costante

- indicare i vincoli di ogni variabile settata dall'utente. Per esempio se chiedo l'età all'utente il dato immesso deve essere un numero ed essere maggiore di 0.

- se si può, indicare il legame tra input e output. Per esempio in "106_stampa_gambero". Input = "Giorgio"; Output = "oigroiG". Nell'output il primo carattere è l'ultimo della stringa di input. Output[0] = Input[len(Input)-1]

Per creare il flow char si deve usare un programma grafico. Io suggerisco "Visio" di Microsoft che avete già nel pacchetto office.

## LINK UTILI

[Stringhe](https://www.pythoncollege.it/tutorial/stringhe-in-python/)

[Liste](https://www.pythoncollege.it/tutorial/liste-in-python/)

[Funzioni](https://www.pythoncollege.it/tutorial/funzioni-in-python/)

## ATTENZIONE ALLE FUNZIONI

**RICORDA**: python si comporta in modo differente in base al tipo di variabile passata come argomento di una funzione:

1) *int, float, string o bool* verrà copiato il valore nella nuova varibile che "vive" dentro nella funzione. La variabile originale non viene modificata.

2) *lista (o meglio un oggetto)* allora stiamo modificando direttamente la variabile originale.

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

**(101_stringa_libro.py)** Stampare una stringa dell'utente in verticale: un carattere per riga.

**(101_stringa_libro_costante.py)** Stampare la stringa "Nel mezzo del cammin di nostra vita" in verticale: un carattere per riga.

**(102_conta_vocali.py)**  Chiedere una stringa all'utente e contare il numero di vocali.

**(103_numeri_in_stringa.py)**  Chiedere una stringa di sole cifre all'utente. Controlla che sia vero. Se si, somma il valore dei numeri presenti (cifra per cifra). Se no chiedi ancora la stringa.

**(104_conta_carattere_stringa)** Chiedere all'utente una stringa ed un carattere. Contare quante volte quel carattere è presente nella stringa.

**(105_conta_n_vocali)** Conta il numero di vocali e stampane il risultato per ogni vocale. Giorgio. a=0, e=0, i=2, o=2, u=0

**(106_stampa_gambero)** Inserisci una parola/frase. Stampa il risultato partendo da destra. Es. Giorgio diventa "oigroiG"

**(107_stringa_consonanti)** Chiedi una stringa all'utente. Stampa la stringa inserita senza le vocali.

**(108_stringa_bilanciata)** Chiedi all'utente 2 stringhe. Controlla che tutti i caratteri presenti nella prima stringa siano presenti nella seconda striga. Non importa la posizione. Stampa il risultato se vero o falso.

**(109_stringhe_bilanciate)** Chiedi all'utente 2 stringhe. Controlla che tutti i caratteri presenti nella prima stringa siano presenti nella seconda striga e che i caratteri della seconda stringa siano presenti nella prima.  Non importa la posizione. Stampa il risultato se vero o falso.

**(110_stringhe_palindorme)** Chiedi all'utente una stringa. Poi controlla che sia palindroma e stampa il risultato.

**(111_conta_occorrenze)** Chiedi all'utente due stringa. Poi conta quante volte la seconda stringa è presente nella prima. Utilizza solo while e non le funzioni "speciali" di python.

**(112_tutto_maiuscolo)** Chiedi una stringa. Poi rendi maiuscole tutte le prime lettere delle parole.

**(113_no_punteggiatura)** Chiedi una stringa. Poi rendi rimuovi tutti i caratteri di punteggiatura. Non utilizzare le funzioni "speciali" di python.

**(114_parola_piu_lunga)** Chiedi una stringa. Trova la parola piu lunga e stampala. Non puoi dividere la stringa.

**(115_AABB)** Stampa 99 righe da 1 a 100 con questa logica: stampa tante A quante sono le unità e  stampa tante B quante sono le decine. Es. "1 > A; 2 > AA; 13 > BAAA; 20 > BB"

------------

### LISTE

**(201_lista_nani)** Crea una lista che contiene tutti nani della favola Biancaneve. Poi chiedi all'utente di trovare tutti i nani. Una volta individuati tutti scrivi "Biancaneve", se l'utente inserisce un nome sbagliato scrivi "riprova".

**(202_lista_reverse)** crea una nuova lista al ma contrario, list1 = [100, 200, 300, 400, 500] deve diventare list2 =[500, 400, 300, 200, 100]. Non usare la funzione reverse(). Poi stampa il risultato.

**(203_merge_list)** crea una nuova lista lista3 prendendo gli elementi sia dalla lista1 che dalla lista2. list1 = ["M", "na", "i", "Ke"] list2 = ["y", "me", "s", "lly"]. Unisci gli elementi che hanno lo stesso indice. Stampa il risultato.

------------

### FUNZIONI

**(301_calcolatrice)** Crea una semplice calcolatrice. Chiedi all'utente che operazione vuole eseguire e i due numeri. Le operazioni sono la somma, la differenza, la moltiplicazione e la divisione. Una volta eseguito il calcolo chiedi se vuole proseguire (Y/N) e so vuole eseguire un altro calcolo. Usa le funzioni. Presta attenzione che l'utente non divida per 0.

------------

### RANDOM

**(401_estrazione_dado)** conta le estrazione di 2 dati fino a quanto non esce il 6-6.

**(402_stampa_estrazione_dado)** Stampa le combinazioni e quante volte sono uscite le combinazioni di 2 dati fino a quanto non esce il 6-6.

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

------------

## LINK DOCUMENTAZIONE PROGETTO DI PROVA

Guardare nella cartella progetti il file "ProgettoVerbiIrregolari.pdf"

------------

## TABELLA VALUTAZIONE PROGETTO

Nel secondo quadrimestre bisognerà pensare, programmare e presentare 3 programmi.

Il voto sarà così composto:

| Valutazione          | Punti |
| -------------------- | ----- |
| Documentazione       | 0-2   |
| Logica/Difficolta    | 1-3   |
| Correttezza e codice | 2     |
| Esposizione          | 0-3   |
| Git                  | 1     |
| Mancata consegna     | -1    |

Una volta concluso il progetto bisognerà creare una presentazione di massimo 20 min in cui si espongono le parti salienti.

Il progetto per poter avere tutti e 3 i punti di "Logica/Difficolta" dovrà essere abbastanza corposo e prevedere una qualche specie di algoritmo e decisione sulle variabili.

Per la documentazione si può seguire il progetto di prova che si trova nella cartella PROGETTI. La documentazione deve includere una analisi dei requisiti, ...

Una volta deciso il proprio progetto si scrive un messaggio (con una descrizione approfondita) nel gruppo TEAMS dove risponderò con APPROVATO/NON APPROVATO.

Se il progetto non viene consegnato entro la scadenza verrà sottratto un punto per ogni lezione di ritardo.

| Documentazione            | Punti |
| ------------------------- | ----- |
| Non adeguata              | 0     |
| Sufficientemente completa | 1     |
| Chiara ed esaustiva       | 2     |

| Difficolta progetto    | Punti |
| ---------------------  | ----- |
| Semplice               | 1     |
| Medio                  | 2     |
| Complesso              | 3     |

**Semplice**: prevede poche variabile o nessun algoritmo particolarmente complesso.

**Medio**: prevede degli algormti che manipolano le variabili secondo criteri logici non banali.

**Complesso**: uso di strutture dati diverse da interi e strighe con algormti che manipolano le variabili secondo criteri logici non banali oppure uso di algoritmi decisamente complicati.

| Correttezza e codice   | Punti |
| ---------------------  | ----- |
| Programma con errori   | 0     |
| Programma funzionante  | 1     |
| Codice ottimizzato     | 2     |

**Codice ottimizzato**: si intende un codice privo di errori, che non abbia ripetizioni facilmente evitabili e scritto seguendo le linee guida.

Bisogna saper spiegare il significato di tutto il codice scritto.

| Esposizione               | Punti |
| ------------------------- | ----- |
| Non adeguata              | 0     |
| Deficitaria               | 1     |
| Sufficientemente completa | 2     |
| Chiara ed esaustiva       | 3     |

**Git**: uso di git per tenere traccia del progetto. 1 Punto.

**Voto**: 11 punti totali

------------

## TABELLA VALUTAZIONE COMPITI

I compiti per casa vengono valutati "in blu", ovvero non hanno un peso diretto nella valutazione finale. Servono allo studente per l'autovalutazione e per indicatore di impegno nella materia.

| Esposizione               | Punti |
| ------------------------- | ----- |
| Non consegnato            | n.c.  |
| Errata                    | 1     |
| Sufficiente, ma con errori| 2     |
| Corretto                  | 3     |

Per creare il flow char si deve usare un programma grafico. Io suggerisco "Visio" di Microsoft che avete già nel pacchetto office.

Quando si consegnano i compiti chiamare il file NomeEsercizio_Cognome.pdf e NomeEsercizio_Cognome.py (o NomeEsercizio_Cognome.txt) es. "15_media_while_Rossi.pdf"

Vedere il riferimento alla sezione "INDICAZIONI FLOW CHAR" per tutte le indicazione da inserire nell'esercizio.
