#Faça um programa que peça os 3 lados de um triângulo. 
# O programa deverá informar se os valores podem ser um triângulo. 
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, 
# isósceles ou escaleno.

#Dicas:

#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior 
#que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;


# Requisitando entrada para o usuário
lado1 = int(input('Digite o primeiro lado: '))
lado2 = int(input('Digite o segundo lado: '))
lado3 = int(input('Digite o terceiro lado:'))

#Primeiro precisamos saber se é um triangulo
if lado1 + lado2 > lado3:
#Agora vamos especificar ao usuario qual triangulo é 
#Triângulo Equilátero: três lados iguais
    if lado1 == lado2 == lado3:
        print('Triângulo Equilátero')
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print('Triângulo Isósceles')
    else:
        print('Triângulo Escaleno')

else:
    print('Não é um triangulo')
