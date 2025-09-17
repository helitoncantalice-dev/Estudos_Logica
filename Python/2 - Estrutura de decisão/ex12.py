#O EXERCICIO ESTAVA COM O ENUNCIOADO MAL FORMULADO 


#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos
# são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 
# 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é 
# descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto
# menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a 
# quantidade de horas trabalhadas no mês.

#Desconto do IR: - Salário Bruto até 900 (inclusive) - isento 
#- Salário Bruto até 1500 (inclusive) - desconto de 5% 
#- Salário Bruto até 2500 (inclusive) - desconto de 10% 
#- Salário Bruto acima de 2500 - desconto de 20%

#Imprima na tela as informações, dispostas conforme o exemplo abaixo.
#No exemplo o valor da hora é 5 e a quantidade de hora é 220.

#Pedindo ao usuario quantidade de horas e valor da sua hora
qnt_horas = float(input('Digite quantas horas você trabalhou : '))
valor_horas = float(input('Digite o valor das suas horas : '))
salario = qnt_horas * valor_horas

#Calculando descontos 
if salario <= 900:
    ir = 0
elif salario <= 1500:
    ir = 5 
elif salario <= 2500:
    ir = 10
else :
    ir = 20








fgts = (salario * 11) / 100
sindicato = (salario * 3) / 100
ir = (salario * ir) / 100
inss = (salario * 10) / 100

total_descontos = sindicato + ir + inss
salario_liquido = salario - total_descontos + fgts

print (f'Salário Bruto (horas * valor ) : R$ {salario:.2f}')
print(f'(-) IR (%)  R$ : {ir}')
print(f'(-) INSS (%) : R$ {inss}')
print(f'Sindicato (%) : R$ {sindicato}')
print(f'FGTS (%)  : R$ {fgts}')
print(f'Salário Líquido  : R$ {salario_liquido:.2f}')