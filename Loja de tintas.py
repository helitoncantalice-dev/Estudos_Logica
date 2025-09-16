#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros 
#quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 
#6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões 
#de 3,6 litros, que custam R$ 25,00.

#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e
#sempre arredonde os valores para cima, isto é, considere latas cheias.




import math

# Solicitar quantidade de M² ao usuário
area = float(input('Digite a quantidade de M²: '))

# Quantidade de litros necessários (com folga de 10%)
litros = (area / 6) * 1.1

# Se o usuário comprar apenas latas 
quantidade_de_latas = math.ceil(litros / 18)
calculo_latas = quantidade_de_latas * 80


# Apenas galões
quantidade_de_galoes = math.ceil(litros / 3.6)
calculo_galoes = quantidade_de_galoes * 25

# Mistura

quantidade_lata_mix = int(litros // 18)
resto = litros - (quantidade_lata_mix * 18)
quantidade_galoes_mix = int(resto / 3.6)
custo_total = (quantidade_lata_mix * 80) + (quantidade_galoes_mix * 25)



#Saída 
print(f'Você vai precisar de {quantidade_de_latas} latas e vai custar: R$ {calculo_latas:.2f}')
print(f'Você vai precisar de {quantidade_de_galoes} galões e vai custar: R$ {calculo_galoes:.2f}')
print(f'Você vai precisar de {quantidade_lata_mix} e de {quantidade_galoes_mix} e vai custar : {custo_total}')
