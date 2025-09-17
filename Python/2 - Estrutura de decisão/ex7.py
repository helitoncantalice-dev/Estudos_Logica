#Faça um programa que leia três números e mostre o maior e o menor deles:

n1 = int(input('Digite o número 1 : '))
n2 = int(input('Digite o número 2 : '))
n3 = int(input('Digite o número 3 : '))

#Verificar maior
if n1 >= n2 and n1 >= n3 :
    print(f'O número {n1} e maior')
elif n2 >= n1 and n2 >= n3 :
    print(f'O número {n2} e maior')
else :
    print(f'O número {n3} e maior')
#Verificando menor
if n1 <= n2 and n1 <= n3 :
    print(f'O número {n1} e o menor')
elif n2 <= n1 and n2 <= n3 :
    print(f'O número {n2} e o menor')
else: 
    print(f'O número {n3} e o menor')