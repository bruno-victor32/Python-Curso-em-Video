#A confederação nacional de natação precisa de um programa
#que leia o ano de nascimento de um atleta e mostre sua categoria
#de acordo com a idade
#até 9 anos: Mirim
#Até 14 anos: infantil
#até 19 anos: Junior
#Até 20 anos:SENIOR
#Acima:Master

from datetime import date
nasc = int(input('Ano de Nascimento: '))
anoAtual =date.today().year
idade = anoAtual - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade > 9 and idade <= 14:
    print('Classificação: INFANTIL')
elif idade > 14 and idade <= 19:
    print('Classificação: JUNIOR')
elif idade == 20:
    print('Classificação: SENIOR')
elif idade > 20:
    print('Classificação: MASTER')