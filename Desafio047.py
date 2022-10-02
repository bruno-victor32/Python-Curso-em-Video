#Crie um programa que mostre na tela todos os
#números pares que estão no intervalo entre 1 e 50

for contador in range(1,51):
    numPares = contador % 2
    if numPares == 0:
        print(contador, end= ' ') #Serve para ter um espaço no final
print('Acabou')

print('Outra forma de fazer o mesmo exercicio')

for cont in range(2, 51, 2):
    print(cont, end=' ')
print('Acabou')