#Faça um programa que pergunte o preço de três produtos e informe qual 
#produto você deve comprar, sabendo que a decisão é sempre pelo mais barato:

produto1 = float(input('Valor do produto 1 :'))
produto2 = float(input('Valor do produto 2 :'))
produto3 = float(input('Valor do produto 3 :'))

if produto1 <= produto2 and produto1 <= produto3:
    print(f'O produto 1 é o mais barato')
elif produto2 <= produto1 and produto2 <= produto3:
    print(f'O produto 2 é o mais barato')
else:
    print(f'O produto 3 é o mais barato')