# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo


num = int(input('Digite um número: '))
tot = 0 # Para eu saber o número de divisiveis
for c in range(1, num + 1):
    if num % c == 0: #Se o numero digitado quando for divisivel pelo contador for igual a 0
        print('\033[033m', end=' ') #Si for divisivel vai ficar amarelo
        tot += 1 #total = total + 1 # Si o número for divisivel e mais um número no total
    else:
        print('\033[31m', end=' ')# Si não for divisivel vai ficar vermelho
    print('{} '.format(c), end=' ') #Aqui estou mandando escrever o número
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))

if tot == 2: #Se ele for divisivel por 1 e por ele mesmo
    print('E por isso que ele é PRIMO!')
else:
    print('E por isso que ele NÃO É PRIMO!')


#Um número primo e somente divisivel por 1 e por ele mesmo, ou sejá o resultado da divisão tem que ser um número inteiro.

