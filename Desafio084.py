''' Faça um programa que leia nome e peso de várias pessoas,
 guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

pessoas = list()
dados = list()
contador = 0
maiorPeso = menorPeso = 0

while True:
    dados.append(str(input('Nome: ')))
    peso = float(input('Peso: '))
    dados.append(peso)
    pessoas.append(dados[:])#Estou fazendo uma copia da lista "dados" e dar um append "inserir" na lista "pessoas"
    dados.clear()
    resp = str(input('Quer continuar? [S/N]')).upper()

    if contador == 0:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso
    contador = contador + 1

    if resp == 'N':
        break
    else:
        if resp != 'S':
            print('Resposta invalida.Tente novamente')
            resp = str(input('Quer continuar? [S/N]')).upper()


print('-=' * 30)

print(f'Ao todo, você cadastrou {contador} pessoas')
print(f'O maior peso foi de {maiorPeso}Kg. Peso de ', end='')
for nome in pessoas:
    if nome[1] == maiorPeso:
        print(f'[{nome[0]}] ', end='')
print()
print(f'O menor peso foi de {menorPeso}Kg. Peso de ', end='')
for nome in pessoas:
    if nome[1] == menorPeso:
        print(f'[{nome[0]}] ', end='')
print()



print('-=' * 30)
print('-=' * 30)
print('RESOLUÇÃO DO PROFESSOR ')
print('-=' * 30)
print('-=' * 30)

temp = list() #Criando uma lista temporaria,vai guardar os dados temporariamente para depois ir para a lista principal
princ = list() #Lista principal
maior = menor = 0
while True: #loop infinito
  temp.append(str(input('Nome: ')))
  temp.append(float(input('Peso: ')))
  if len(princ) == 0: #Si eu não tiver cadastrado ninguem ainda
    maior = menor = temp[1] #O maior valor vai ser a mesma coisa que o menor valor que e a mesma coisa que temp na posição que nesse caso e o peso
  else:
    if temp[1] > maior: #Si temp[1] que e o peso for maior que o maior valor
      maior = temp[1] #maior passa a ser o temp[1]
    if temp[1] < menor:
      menor = temp[1]
  princ.append(temp[:])
  temp.clear()#Limpando o temp
  resp = str(input('Quer continuar? [S/N]'))
  if resp in 'Nn': #Se resposta for igual a 'N' ou 'n'
    break

print('-=' * 30)
print(f'Ao todo,você cadastrou {len(princ)} pessoas.') # Mostrando o tamanho do cadastro principal
print(f'O maior peso foi de {maior}kg. Peso de ' , end='')
for p in princ: #Para cada pessoa que está na lista principal
  if p[1] == maior: #Si o peso for igual ao maior valor
    print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {menor}kg. Peso de ' , end='')
for p in princ: #Para cada pessoa que está na lista principal
  if p[1] == menor: #Si o peso for igual ao menor valor
    print(f'[{p[0]}]', end='')
print()






