''' Faça um programa que ajude um jogador da MEGA SENA
a criar palpites.O programa vai perguntar quantos jogos
serão gerados e vai sortear 6 números entre 1 e 60 para
cada jogo, cadastrando tudo em uma lista composta.'''

#from random import randint #Importar somente o metodo de randomizar
#jogofinal = []
#palpiteinicial = []
#print('-' * 40)
#print('\t\tJOGA NA MEGA SENA')
#print('-' * 40)
#resp = int(input('Quantos jogos você quer que eu sorteie? '))
#print('-=-=-= SORTEANDO 4 JOGOS -=-=-=')
#for contador in range(0, resp + 1):
        #valores = (randint(0,60),randint(0,60),randint(0,60),randint(0,60),randint(0,60),randint(0,60),randint(0,60))
        #palpiteinicial.append(valores)
#jogofinal.append(palpiteinicial[:])

#print(f'{contador}º{jogofinal}')


from random import randint
from time import sleep
lista = list() #Criando uma lista
jogo = list() #A lista jogo vai ser composta de outra lista que são os sorteios
print('-' * 30)
print('         JOGA NA MEGA SENA        ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant: #Enquanto o total for menor que a quantidade de jogos que eu quero que sorteie
        cont = 0 #Criando uma variavel contador
        while True: #Enquanto for verdadeiro
                num = randint(1, 60) #Aqui estou sorteando números
                if num not in lista: #Verificando si o número sorteado não está na lista,caso não esteja vai ser adicionado a lista
                        lista.append(num) #Adicionando o número sorteado na lista
                        cont = cont + 1 #Se for adicionado na lista ,vamos somar mais um no contador
                if cont >= 6: #Se o contador for maior que 6, ou sejá, si foi adicionado mais que 6 números
                        break #O looping vai parar
        lista.sort() #Colocando os números em ordem crescente
        jogo.append(lista[:]) #Estou fazendo uma copia da lista e colocando na lista chamada jogos
        lista.clear() #Depois que eu crio uma copia da lista eu apago a lista,pois os dados estarão na lista chamada jogos
        tot = tot + 1 #E para o programa não entrar em loop infinito
        #print(f'Os números sorteados foram {lista}')
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
#print(f'Os números sorteados foram {jogo}')
#For para cada elemento da lista de jogos
for i, l in enumerate(jogo): #Para cada indice, com a lista enumerate dos jogos
        print(f'Jogo {i+1}: {l}')
        sleep(1) #vAI AGUARDAR UM SEGUNDO PARA MOSTRAR A OUTRA SEQUENCIA DE SORTEIO
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
