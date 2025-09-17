#Faça um programa que pergunte em que turno você estuda. Peça para digitar:

#M - Matutino
#V - Vespertino
#N - Noturno.
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!",
#Conforme o caso.

turno = str(input('Digite seu turno "m", "v" ou "n" : ')).lower()

if turno in 'mvn':
    if turno == 'm':
        print('Bom dia !')
    elif turno == 'v':
        print('Boa tarde !')
    else:
        print('Boa noite !')
else:
    print('Valor inválido')