''' Escreva um programa que leia um número N inteiro qualquer e mostre na tela
os N primeiros elementos de uma Sequência de Fibonacci. '''

print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? '))
primeiroTermo = 0
segundoTermo = 1
print('~' * 30)
print('{} -> {}'.format(primeiroTermo, segundoTermo), end='')
contador = 3 #Como já mostrei o primeiro termo e o segundo termo, o meu contador vai iniciar no 3
while contador <= n:
    terceiroTermo = primeiroTermo + segundoTermo
    print(' -> {}'.format(terceiroTermo), end='')
    primeiroTermo = segundoTermo
    segundoTermo = terceiroTermo
    contador = contador + 1
print(' -> FIM')
print('~' * 30)