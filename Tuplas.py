#Uma variavel que armazena varios valores pode ser uma Tupla
#Toda tupla e entre parenteses ()

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim' ) #Aqui criei uma variavel composto, uma TUPLA
print(lanche) #Aqui vai mostrar todos os valores que estão armazenados na variavel composta

print('=' * 30)

print(lanche[0])#Aqui vai mostrar somente o HAMBURGUER,pois ele e o indice 0
print(lanche[1]) #Aqui vai mostrar somente o SUCO
print(lanche[2]) #Aqui vai mostrar somente o PIZZA
print(lanche[3]) #Aqui vai mostrar somente o PUDIM

print('=' * 30)

print(lanche[-1])#Vai mostrar o ultimo elemento que e o PUDIM
print(lanche[-2])#Vai mostrar a PIZZA
print(lanche[-3])#Vai mostrar o SUCO
print(lanche[-4])#Vai mostrar o HAMBURGUER

print('=' * 30)

print(lanche[1:3])#Aqui ele vai mostrar somente SUCO E PIZZA,porque o elemento 3 que seria PUDIM e ignorado quando eu faço o fatiamento
print(lanche[2:])#Começa da PIZZA e vai até o final,então vai mostrar PIZZA E PUDIM

print('=' * 30)

print(lanche[:2])#Me mostre do inicio até o elemento 2,lembrando que ele vai ignorar o elemento 2.Vai mostrar HAMBURGUER E SUCO
print(lanche[-1:])#Vai começar do PUDIM e vai até o final
print(lanche[-2:])#Vai começar na PIZZA e vai até o final
print(lanche[-3:])#Vai começar no SUCO e vai até o final
print(lanche[-4:])#Vai começar no HAMBURGUER e vai até o final

print('=' * 30)
print('-' * 30)
print('=' * 30)

#TUPLAS SÃO IMUTÁVEIS
#Não posso modificar a tupla quando o programa está em execução
#Quando não está em execução o programa eu posso modificar a tupla


for comida in lanche:#Para cada comida em lanche
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
print('=' * 30)
print('-' * 30)
print('=' * 30)
print(len(lanche))
print('=' * 30)
print('-' * 30)
print('=' * 30)
for contador in range(0, len(lanche)): #O range vai começar do indice 0 até o ultimo valor da Tupla.Vai ignorar o ultimo valor
    print(f'Eu vou comer {lanche[contador]}')
print('=' * 30)
print('-' * 30)
print('=' * 30)
for contador in range(0, len(lanche)):
    print(contador)
print('=' * 30)
print('-' * 30)
print('=' * 30)
for contador in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[contador]} na posição {contador} ')
print('Comi pra caramba!')
print('=' * 30)
print('-' * 30)
print('=' * 30)
for posicao,  comida in enumerate(lanche):#Com o enumerate da tanto o DADO quanto a POSIÇÃO
    print(f'Eu vou comer {comida} na posição {posicao}')
print('Comi pra caramba!')
print('=' * 30)
print('-' * 30)
print('=' * 30)
print(sorted(lanche))#Estou mostrando o lanche em ordem,ele não vai alterar sua tupla
print('=' * 30)
print('-' * 30)
print('=' * 30)
#Outro exemplo
a = (2,5,4)
b = (5,8,1,2)
print(a)
print(b)


print('-' * 30)
c = a + b #Vai juntar a tupla A com a tupla B
d = b + a #Vai juntar a tupla B com a tupla A
print(d)
print(c)
print(f'tem {len(c)} elementos a tupla C')#Vai me mostrar o tamanho dessa tupla
print(f'O  5 está aparecendo { c.count(5)} vezes na tupla C') #Quantas vezes está aparecendo o numero 5 dentro de C
print(f'O número 8 esta na posição { c.index(8)}') #O index de 8, e saber em que posição está o numero 8 dentro C.Aqui pega a primeira ocorrencia
print(f'O número 2 esta na posição { d.index(2,4)} a partir da posição 4') #O index de 2, e saber em que posição está o numero 2 dentro D.Aqui pega a  ocorrencia a partir da posição 4
print(f'O número 5 esta na posição { d.index(5,1)} a partir da posição 1') #O index de 2, e saber em que posição está o numero 5 dentro D.Aqui pega a  ocorrencia a partir da posição 1


print('=' * 30)
print('-' * 30)
print('=' * 30)
pessoa = ('Gustavo', 39, 'M',99.88)# Posso ter dados de tipos diferentes dentro das minhas tuplas
print(pessoa)


print('=' * 30)
print('-' * 30)
print('=' * 30)
#Apagando a Tupla
humanos = ('Barbara', 49, 'F',100.88)# Posso ter dados de tipos diferentes dentro das minhas tuplas
del(humanos) #Estou deletando,apagando a Tupla inteira.Não consigo deletar um item da Tupla, somente a tupla inteira
