'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
 No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas
 posições na lista. '''

maior = 0
menor = 0
valores = list()#Criando uma lista.Podemos também criar uma lista assim "valores = []"

for contador in range(0, 5): #Quero ler 5 valores
    valores.append(int(input(f'Digite um valor para a Posição {contador}:'))) #Colocando os valores na lista
    if contador == 0: #Si for o primeiro valor lido, ele vai ser o maior e o menor valor
        maior = valores[contador]
        menor = valores[contador]
    else: #Senão for o primeiro valor lido
        if valores[contador] > maior:
            maior = valores[contador]
        if valores[contador] < menor:
            menor = valores[contador]
print('=-='* 30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições', end='')
for indice, valor in enumerate(valores): #Para mostrar em que posição está o maior valor
    if valor == maior:
        print(f' {indice}... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições', end='')
for indice, valor in enumerate(valores):
    if valor == menor:
        print(f' {indice}...', end='')
print()

print('=-=' * 30)
print('=-=' * 30)
print('=-=' * 30)

valoresDigitador = list()
for contador in range(0, 5):
    valoresDigitador.append(int(input(f'Insira um número para a posição {contador}: ')))
print('-' * 35)
print('Você inseriu os valores: ', end='')
for valor in valoresDigitador:
    print(valor, end=' ')
print(f'\nO menor valor é {min(valoresDigitador)} nas posições  ', end='')
for indice, valor in enumerate(valoresDigitador):
    if valor == min(valoresDigitador):
        print(indice, end='... ')
print(f'\nO maior valor é {max(valoresDigitador)} nas posições  ', end='')
for indice, valor in enumerate(valoresDigitador):
    if valor == max(valoresDigitador):
        print(indice, end='... ')
print()
