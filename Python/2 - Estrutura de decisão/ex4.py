#Faça um programa que verifique se uma letra digitada é vogal ou consoante.
#.lower() esta sendo utilizado para evitar letras maiusculas e possiveis erros
letra_digitada = str(input('Digite a letra: ')).lower()

# Estrutura condicional 
if letra_digitada in 'aeiou':
    print ('Essa letra é uma vogal')
else:
    print('Essa letra não é uma vogal')