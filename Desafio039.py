#Faça um programa que leia o ano de nascimento de um jovem e
#informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar
#Se é a hora de se alistar
#Se já passou do tempo de alistamento
#Seu programa também deverá mostrar o tempo que falta ou que passou
#do prazo

from datetime import date
nasc = int(input('Ano de nascimento: '))
anoAtual =date.today().year
idade = anoAtual - nasc

print('Quem nasceu em {} tem {} anos em {}'.format(nasc,idade,anoAtual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade > 18:
    alistamento = idade - 18
    anoAlistamento = anoAtual - alistamento
    print('Você já deveria ter se alistado há {} anos'.format(alistamento))
    print('Seu alistamento foi em {}'.format(anoAlistamento))
elif idade < 18:
    alistamento = 18 - idade
    anoAlistamento = anoAtual + alistamento
    print('Ainda faltam {} ano(s) para o alistamento'.format(alistamento))
    print('Seu alistamento será em {}'.format(anoAlistamento))

