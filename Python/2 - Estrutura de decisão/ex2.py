#Faça um programa que peça um valor e mostre
#na tela se o valor é positivo ou negativo.

valor = int(input('Digite um valor: '))

if valor < 0 :
    print(f'O valor {valor} e negativo')
elif valor == 0:
    print(f'O valor {valor} não é positivo nem negativo !')
else :
    print(f'O valor {valor} e positivo')