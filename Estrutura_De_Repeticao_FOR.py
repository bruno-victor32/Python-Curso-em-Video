for contador in range(1, 6): #
    print('Oi') #Vou repetir a palavra oi 5 vezes,porque de 1 até 6,o contador vai fazer de 1 até 5 e na sexta posição vai parar, ele n vai considerar o ultimo número
print('Fim')

print('-=' * 10)

for contador in range(0, 6):
    print('Oi')
print('Fim')

print('-=' * 10)

for contador in range(0, 6):
    print(contador)
print('Fim')

print('-=' * 10)

for contador in range(1, 7):
    print(contador)
print('Fim')

print('-=' * 10)

#Para fazer uma contagem de 6 até 0, para contar para tras coloca -1
for contador in range(6, 0, -1):
    print(contador)
print('Fim')

print('-=' * 10)

for contador in range(0, 7):
    print(contador)
print('Fim')

print('-=' * 10)

#Fazer a contagem pulando de 2 em 2
for contador in range(0, 7,2):
    print(contador)
print('Fim')

print('-=' * 10)

n = int(input('Digite um número: '))
for c in range(0, n + 1):# o "N + 1" SERVE PARA A CONTAGEM PARA NO NUMERO QUE EU DIGITAR, SI POR EXEMPLO EU COLOCAR 9 A CONTAGEM VAI PARAR NO 8, POR ISSO EU SOMA +1 PARA EXATAMENTE NO NÚMERO QUE DIGITEI
    print(c)
print('FIM')

print('-=' * 10)

n = int(input('Digite um número: '))
for c in range(0, n):
    print(c)
print('FIM')

print('-=' * 10)

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
for c in range(inicio, fim, passo):
    print(c)
print('FIM')

print('-=' * 10)

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
for c in range(inicio, fim + 1, passo):
    print(c)
print('FIM')

print('-=' * 10)

for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('Fim')

print('-=' * 10)

soma = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    soma = soma + n   # e a mesma coisa fazer soma += n
print('O somatório de todos os valores foi {}'.format(soma))


