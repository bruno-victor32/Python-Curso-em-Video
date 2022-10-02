#Criando uma Tupla
num1 = (2, 5, 9, 1)
#num1[2] = 3
print(num1)

print('-=-' * 10)
 #Criando uma Lista
num = [2, 5, 9, 1]
num[2] = 3 #Aqui o numero 9 que está no indice 2 vai ser mudado para o numero 3
num.append(7) #Aqui estou adicionando o valor 7 ao elemento,adicionando ao final da minha lista
num.sort() #Vai ordenar todos os valores
num.sort(reverse=True) #Vai ordenar todos os valores em ordem reversa
num.insert(2, 0) #Adicionando valores.Eu quero na posição 2 inserir o valor 0
num.pop() #Eliminando o ultimo valor
num.pop(2) #Eliminando o elemento que está no indice 2
print(num)
print(f'Essa lista tem {len(num)} elementos.') #O len permite descobrir o tamanho de uma lista

print('-=-' * 10)
#Criando outra lista
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2,2)
num.remove(2)#O remove procura do inicio da lista, a primeira ocorrência do valor que vc mando eliminar e ele elimina.Ele não varre até o final para eliminar todos os numeros iguais
print(num)
print(f'Essa lista tem {len(num)} elementos')

print('-=-' * 10)
#Criando outra lista
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2,2)
if 4 in num: #Si o numero 4 estiver na lista ele remove
    num.remove(4)
else:#senão
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')

print('-=-' * 10)
#Criando outra lista
valores = list() #valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores: #Para cada elemento da minha lista
    print(f'{v}...',end='')
print('\n') #Pulei uma linha

for chave, valor in enumerate(valores):
    print(f'\nNa posição {chave} encontrei o valor {valor}!')
print('Cheguei ao final da lista')

print('-=-' * 10)
#Criando outra lista
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for chave, valor in enumerate(valores):
    print(f'\nNa posição {chave} encontrei o valor {valor}!')
print('Cheguei ao final da lista')

print('-=-' * 10)
#Criando outra lista
a = [2,3,4,7]
b = a #Dessa forma não e uma copia e sim uma LIGAÇÃO
b[2] = 8 #Vou mudar o numero 4 para 8, já que o número 4 encontra-se no indice 2
print(f'Lista A: {a}')
print(f'Lista B: {b}')

#A partir do momento que eu igualo uma lista na outra
#O python gera uma ligação entre elas

print('-=-' * 10)
#Criando outra lista
a = [1, 2, 3, 4]
b = a[:]#b receba todos os itens de a.Vou pegar todos os valores de "a" e jogar em "b", aqui estou criando uma copia
b[2] = 8 #Agora vou mudar o valor do indice 2
print(f'Lista A: {a}')
print(f'Lista B: {b}')