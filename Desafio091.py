'''Crie um programa onde 4 jogadores joguem um dado e
tenham resultados aleatórios. Guarde esses resultados em um
 dicionário em Python. No final, coloque esse dicionário em
  ordem, sabendo que o vencedor tirou o maior número no dado.'''

from random import randint #Metodo para gerar números aleatorios
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}       #Aqui estou criando um dicionario e já colocando os valores sorteados nele
ranking = list() #Criando uma lista vazia
print('Valores sorteados: ')
for k, v in jogo.items(): # para chave e valor do dicionario jogo
    print(f'{k} tirou {v} no dado.')
    sleep(1)#Aqui permite demora 1 segundo para imitar que o programa está processando
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #Ordenando
print('-' * 30)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')