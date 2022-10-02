'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no
 final do jogo.'''

from random import randint #Importa da biblioteca random o metodo randint
v = 0 #vitoria
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10) #Sorteando um valor
    total = jogador + computador #Realizando a soma do valor digitado e do valor sorteado
    tipo = ' ' #O tipo vai iniciar valendo 0
    while tipo not in 'PI': #Enquanto a variavel tipo  for "P" OU "I" maiusculo, vai ser feito a logica
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0] #Aqui estou pegando somente a primeira letra
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}',end='')
    if total % 2 == 0:
        print(' DEU PAR')
    else:
        print(' DEU IMPAR')
    if tipo == 'P': #Se o tipo for igual a par
        if total % 2 == 0:
            print('Você VENCEU!')
            v = v + 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':#Se o tipo for igual a ímpar
        if total % 2 == 1:
            print('Você VENCEU!')
            v = v + 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAMER OVER! Você venceu {v} vezes')