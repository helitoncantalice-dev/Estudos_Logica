#Faça um programa que leia três números e mostre o maior deles:

n1 = int(input('Digite o número 1 : '))
n2 = int(input('Digite o número 2 : '))
n3 = int(input('Digite o número 3 : '))

if n1 >= n2 and n1 >= n3 :
    print(f'O maioir número e {n1}')
elif n2 >= n1 and n2 >= n3:
    print(f'O maior número e {n2}')
else:
    print(f'O maior número e {n3}')