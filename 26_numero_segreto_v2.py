numero=0
i = 1
numero_segreto = 80

while True:
    numero=int(input('Inserisci il numero: '))
    
    if (numero == numero_segreto):
        break
    result = numero - numero_segreto

    suggerimento_1 = ""
    suggerimento_2 = ""

    if (result > 0):
        suggerimento_1 =  "piu grande"
    else:
        suggerimento_1 =  "piu piccolo"
        result = result * -1
    
    if (result >= 20):
        suggerimento_2 = " - oceano"
    else:         
        if (result > 10 ):
            suggerimento_2 = " - fuochino"
        else:
            suggerimento_2 = " - fuoco"

    print(suggerimento_1 + suggerimento_2)
    i = i + 1

print('Complimenti, hai indovinato in ' + str(i) + "tentativi")