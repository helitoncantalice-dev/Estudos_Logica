#Faça um programa que peça uma data no formato dd/mm/aaaa 
#e determine se a mesma é uma data válida.

data = input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = map(int, data.split("/"))

# Inicializando variável de validação
data_valida = True

# Verificando mês
if mes < 1 or mes > 12:
    data_valida = False
else:
    # Janeiro, março, maio, julho, agosto, outubro, dezembro → 31 dias
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        if dia < 1 or dia > 31:
            data_valida = False
    # Abril, junho, setembro, novembro → 30 dias
    elif mes in [4, 6, 9, 11]:
        if dia < 1 or dia > 30:
            data_valida = False
    # Fevereiro
    elif mes == 2:
        # Verifica se ano é bissexto
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            if dia < 1 or dia > 29:
                data_valida = False
        else:
            if dia < 1 or dia > 28:
                data_valida = False

# Saída
if data_valida:
    print(f"A data {data} é válida.")
else:
    print(f"A data {data} é inválida.")