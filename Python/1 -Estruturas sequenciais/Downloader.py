#Faça um programa que peça o tamanho de um arquivo para download 
#(em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o 
#tempo aproximado de download do arquivo usando este link (em minutos).
import math
# Precisamos pedir o tamanho do arquivo (MB)
arquivo = float(input('Qual o tamanho do arquivo em MB : '))

# Agora precisamos pedir a velocidade da internet do usuário em (Mbps)
v_internet = float(input('Informe a velocidade da internet em Mbps : '))

# Precisamos primeiro converter a velocidade da internet por sengundo para saber
# quanto tempo demora para atingir os MB necessario

#Aqui nos convertemos Mbps para MB/s
v_internet_convertida = v_internet / 8
print(f'{v_internet_convertida}Mb/s')

# Sabendo a quantidade de MB's por segundo da conexão basta dividirmos pelo valor do arquivo
calculo_tempo = arquivo / v_internet_convertida
print(f'{calculo_tempo:.2f} segundos')
calculo_minutos = math.ceil(calculo_tempo / 60)
print(f'{calculo_minutos} minutos (Aredondando para cima)')

