#Faça um programa que verifique se uma letra digitada é "F" ou "M". 
#Conforme a letra escrever:

#F - Feminino
#M - Masculino
#Sexo Inválido.
#.lower() esta sendo utilizado para evitar letras maiusculas e possiveis erros
letra_digitada = str(input('Digite seu sexo M/F : ')).lower()

# Etapa de verificação

if letra_digitada == 'f':
    print('Você e do sexo feminino')
elif letra_digitada == 'm': 
    print('Você e do sexo masculino')
else:
    print('Sexo inválido')