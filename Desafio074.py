''' Crie um programa que vai gerar cinco números aleatórios e
colocar em uma tupla. Depois disso, mostre a listagem de números
gerados e também indique o menor e o maior valor que estão na tupla.'''


from random import randint #Importar somente o metodo de randomizar
numeros = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))#Tupla
print('Os valores sorteados foram: {}'.format(numeros))
print(f'O maior valor sorteado foi {max(numeros)}')#Estamos usando metodo especifico das Tuplas
print(f'O menor valor sorteado foi {min(numeros)}')

print('-=-' * 30)
print('Os valores sorteados foram: ',end='')
for n in numeros:
    print(f'{n}',end=', ')





