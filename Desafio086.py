''' Crie um programa que declare uma matriz de dimensão 3x3 e preencha
com valores lidos pelo teclado. No final, mostre a matriz na tela, com
a formatação correta.'''

#Dentro de cada lista terá 3 valores vazios,para não necessitar usar append
matriz = [[0,0,0],[0,0,0],[0,0,0]] #Criando uma lista com 3 lista dentro
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}] : '))

print('-=' * 30)
#Para mostrar a estrutura na tela
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]',end='')#Vou formatar esse valor com 5 casas decimais(espaços) centralizado
    print()

