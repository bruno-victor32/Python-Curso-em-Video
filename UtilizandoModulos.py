print('Calcular a raiz quadrada de um número\n')

import math #Importando uma biblioteca,nesse caso estou importando todas as funcionalidades
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A  raiz de {} é igual a {}'.format(num, raiz))

print("============================================\n")

print('Calcular a raiz quadrada de um número e arredondar para baixo\n')

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))

print("============================================\n")

print('Calcular a raiz quadrada de um número e arredondar para cima\n')

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))

print("============================================\n")

print('Calcular a raiz quadrada importando somente a funcionalidade de raiz quadrada\n')

from math import sqrt #Nesse caso estou importando somente a funcionalidade de raiz quadrada
num = int(input('Digite um número: '))
raiz = sqrt(num) #Importando dessa maneira eu não preciso fazer referencia a biblioteca math,posso colocar diretamente a função
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

print("============================================\n")

print('Calcular a raiz quadrada importando somente a funcionalidade de raiz quadrada e arredondar para baixo\n')

from math import sqrt,floor #Nesse caso estou importando somente a funcionalidade de raiz quadrada e de arredondamento para baixo
num = int(input('Digite um número: '))
raiz = sqrt(num) #Importando dessa maneira eu não preciso fazer referencia a biblioteca math,posso colocar diretamente a função
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))

print("============================================\n")

print('Gerar um número aleatorio')

import random #A biblioteca random permite eu gerar numeros aleatorios
num = random.random() #O metodo random da classe randow ele gera um número aleatorio entre 0 e 1,um numero float, um numero real entre 0 e 1
print(num)

print("============================================\n")

print('Gerar um número aleatorio entre 1 até 10')
#Caso você queira você pode colocar um randint que e randomizar um numero inteiro

import random #A biblioteca random permite eu gerar numeros aleatorios
num = random.randint(1,10) #Vou gerar um número aleatorio entre 1 e 10
print(num)

print("============================================\n")

print('Utilizando uma biblioteca que será baixada da internet\n')

import emoji
print(emoji.emojize('Olá,Mundo :earth_americas:', use_aliases=True))
print(emoji.emojize('Sou gato :sunglasses:', use_aliases=True))