#Faça um programa que lê as duas notas parciais obtidas por um aluno numa 
# disciplina ao longo de um semestre, e calcule a sua média. A atribuição de 
# conceitos obedece à tabela abaixo:

#Média de Aproveitamento  Conceito
#Entre 9.0 e 10.0         A
#Entre 7.5 e 9.0          B
#Entre 6.0 e 7.5          C
#Entre 4.0 e 6.0          D
#Entre 4.0 e zero         E
#O algoritmo deve mostrar na tela as notas, a média, o conceito 
# correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou 
# “REPROVADO” se o conceito for D ou E.

nota_1 = int(input('Digite a primeira nota : '))
nota_2 = int(input('Digite a segunda nota : '))
media = (nota_1 + nota_2 ) / 2
if media >= 9:
    situacao = 'APROVADO'
    conceito = 'A'
elif media >= 7.5:
    situacao = 'APROVADO'
    conceito = 'B'
elif media >= 6.0:
    situacao = 'APROVADO'
    conceito = 'C'
elif media >= 4:
    situacao = 'REPROVADO'
    conceito = 'D'
else :
    situacao = 'REPROVADO'
    conceito = 'E'



print(f'Suas notas são {nota_1} e {nota_2}')
print(f'Sua média e : {media:.2f}')
print(f'Seu conceito é {conceito}')
print(f'Sua situação é {situacao}')