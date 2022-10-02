'''Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''

# Resolvendo o desafio utilizando modulos

from math import factorial #Existe um metodo para calculo de fatorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))

#Outra maneira de fazer o exercicio
print('=-=' * 15)

n = int(input('Digite um número para calcular seu Fatorial: '))
contador = n
fatorial = 1
print('Calculando {}! = '.format(n), end='')
while contador > 0:
    print('{} '.format(contador), end=' ') #O end='' serve para não pular de linha
    print(' x ' if contador > 1 else ' = ', end='') #Mostrar o "x" se o contador for maior que 1, se não for maior que 1 vai ser colocado "="
    fatorial = fatorial * contador
    contador = contador - 1
print('{}'.format(fatorial))