'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[0,0,0],[0,0,0],[0,0,0]]
par = 0
valoresTerceiraColuna = 0
for linha in range(0, 3):
    for coluna in range(0,3):
        valores = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        matriz[linha][coluna] = valores  # Estou adicionando o valor digitado a matriz
        if valores % 2 == 0: #Si o resultado da divisão for igual a 0,significa que o número digitado e PAR
            par = par + valores #Somando os valores
    valoresTerceiraColuna = valoresTerceiraColuna + matriz[linha][2] #Como minha coluna e sempre fixa, eu coloco no for da linha que não e fixa

print('-=' * 30)

for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]',end='')
    print()

print('-=' * 30)
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {valoresTerceiraColuna}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')


print('-=' * 30)
print('-=' * 30)
print('RESOLUÇÃO DO PROFESSOR')
print('-=' * 30)
print('-=' * 30)

somaPar = maiorValor = somaColuna = 0
#Dentro de cada lista terá 3 valores vazios,para não necessitar usar append
matriz = [[0,0,0],[0,0,0],[0,0,0]] #Criando uma lista com 3 lista dentro
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}] : '))

print('-=' * 30)
#Para mostrar a estrutura(matriz) na tela
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]',end='')#Vou formatar esse valor com 5 casas decimais(espaços) centralizado
        if matriz[linha][coluna] % 2 == 0: #Se o número que acabou de exibido na tela for par
            somaPar = somaPar + matriz[linha][coluna]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {somaPar}')
for linha in range(0,3): #Como a coluna e fixa eu faço um for para a linha
    somaColuna = somaColuna + matriz[linha][2] #Somente a linha que vai variar
print(f'A soma dos valores da terceira coluna é {somaColuna}')
for coluna in range(0,3):
    if coluna == 0: #Significa que é a primeira coluna
        maiorValor = matriz[1][coluna] #Si for a primeira coluna e o primeiro valor digitado,vai ser o maior valor
    else:#senao
        if matriz[1][coluna] > maiorValor: #Estou comparando si o maior valor até o momento e maior que o valor digitado agora
            maiorValor = matriz[1][coluna]
print(f'O maior valor da segunda linha é {maiorValor}.')