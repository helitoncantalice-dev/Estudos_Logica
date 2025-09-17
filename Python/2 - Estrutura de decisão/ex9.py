#Faça um programa que leia três números e mostre-os em ordem decrescente:

n1 = int(input('Digite o número 1 : '))
n2 = int(input('Digite o número 2 : '))
n3 = int(input('Digite o número 3 : '))

#Primeiro vamos verificar se N1 e maior
if n1 >= n2 and n1 >= n3:
#Agora sabemos que n1 e maior 
    if n2 >= n3:
#se n2 for maior ele aparece primeiro
        print(n1, n2, n3)
#se não n3 e maior e ele aparece primeiro
    else:
        print(n1, n3, n2)

#Verificando se n2 e maior
elif n2 >= n1 and n2 >= n3:
#n2 aparece primeiro e n1 aparece em segundo 
    if n1 >= n3:
        print(n2, n1, n3)
#n2 apare primeiro n3 segundo e n1 ultimo
    else:
        print(n2, n3, n1)

else:
#n3 aparece primeiro
    if n1 >= n2:
#mesma lógica
        print(n3, n1, n2)
#mesma lógica
    else:
        print(n3, n2, n1)
