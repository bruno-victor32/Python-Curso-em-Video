'''Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores'''

from datetime import date
anoAtual = date.today().year #Pegando o ano atual
totalizarVelho = 0
totalizarNovo = 0 #Contador de pessoas que tem menos de 18 anos
for pessoa in range(1,8):
    ano = int(input('Em que ano a {}º pessoa nasceu? '.format(pessoa)))
    ano = anoAtual - ano
    if ano >= 18:
        totalizarVelho = totalizarVelho + 1
    elif ano < 18:
        totalizarNovo = totalizarNovo + 1
print('\n')
print('Ao todo tivemos {} pessoas maiores de idade'.format(totalizarVelho))
print('E também tivemos {} pessoas menores de idade'.format(totalizarNovo))

