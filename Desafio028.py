#Escreva um programa que faça o computador "pensar"
#em um número inteiro entre 0 e 5 e peça para o
#usuário tentar descobrir qual foi o número escolhido
#pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu

import time
from random import randint
print('-=- '* 10)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=- '* 10)
valorSorteado = randint(0,5) #Gerando um número aleatorio
valorDigitado = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
time.sleep(10) #Faz o programa dar um delay
if valorSorteado == valorDigitado:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {}  e não no {}!'.format(valorSorteado, valorDigitado))