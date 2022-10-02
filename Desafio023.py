#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados

num = int(input('Digite um número: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))

#Não dá para resolver esse exercicio utilizando split,porque falta ainda aprender sobre listas