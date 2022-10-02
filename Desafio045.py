#Crie um programa que faça o computador jogar Jokenpô com você

from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('Suas opções: ')
print('[ 0 ] PEDRA ')
print('[ 1 ] PAPEL ')
print('[ 2 ] TESOURA ')
jogador = int(input('Qual é a sua jogada? '))
print('-='*15)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*15)
if computador ==0: #computador jogou PEDRA
    if jogador == 0:#Jogador jogou PEDRA
        print('Empate')
    elif jogador == 1:#Jogador jogou PAPEL
        print('JOGADOR VENCE')
    elif jogador == 2:#Jogador jogou TESOURA
        print('COMPUTADOR VENCEU')
    else:
        print(' JOGADA INVÁLIDA!')
elif computador == 1: #computador jogou PAPEL
    if jogador == 0:#Jogador jogou PEDRA
        print('COMPUTADOR VENCEU')
    elif jogador == 1:#Jogador jogou PAPEL
        print('Empate')
    elif jogador == 2:#Jogador jogou TESOURA
        print('JOGADOR VENCE')
    else:
        print(' JOGADA INVÁLIDA!')
elif computador == 2: #computador jogou TESOURA
    if jogador == 0:#Jogador jogou PEDRA
        print('JOGADOR VENCE')
    elif jogador == 1:#Jogador jogou PAPEL
        print('COMPUTADOR VENCEU')
    elif jogador == 2:#Jogador jogou TESOURA
        print('Empate')
    else:
        print(' JOGADA INVÁLIDA!')
