#Peça ao usuário para digitar uma hora no formato HH:MM.
#Verifique se a hora é válida:
#Horas (HH) devem estar entre 0 e 23.
#Minutos (MM) devem estar entre 0 e 59.
#Informe ao usuário se a hora é válida ou inválida.
#Bônus: Se a hora for válida, informe se é:
#Manhã → 05:00 a 11:59
#Tarde → 12:00 a 17:59
#Noite → 18:00 a 21:59
#Madrugada → 22:00 a 04:59

#Primeiro precisamos digitar uma hora no formato HH:MM
horas = input('Digite as horas no formato HH:MM: ')
hora, minuto = map(int, horas.split(':'))

# Verificação de validade
if hora < 0 or hora > 23:
    print("Hora inválida")
elif minuto < 0 or minuto > 59:
    print("Minuto inválido")
else:
    # Hora válida, agora verificamos o período do dia
    if hora >= 5 and hora <= 11:
        print("Manhã")
    elif hora >= 12 and hora <= 17:
        print("Tarde")
    elif hora >= 18 and hora <= 21:
        print("Noite")
    else:
        print("Madrugada")