''' Crie um programa onde o usuário possa digitar sete valores numéricos
 e cadastre-os em uma lista única que mantenha separados os valores pares
  e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''

listaCompleta = list()
par = list()
impar = list()
for contador in range(1,8):
    valores =int(input(f'Digite o {contador}°. valor: '))
    if valores % 2 == 0:
        par.append(valores)
    else :
        impar.append(valores)
impar.sort()
par.sort()
listaCompleta.append(par)
listaCompleta.append(impar)
print('-=' * 30)
print(f'Os valores pares digitados foram: {listaCompleta[0]}')
print(f'Os valores ímpares digitados foram: {listaCompleta[1]}')

print('-=' * 30)
print('-=' * 30)
print('RESOLUÇÃO DO PROFESSOR')
print('-=' * 30)
print('-=' * 30)

num = [[], []] #No python estou declarando uma lista, onde dentro dessa lista eu tenho outras 2 listas internas.Uma lista para os números pares e outra lista para os números impares
valor = 0
for contador in range(1, 8):
  valor  = int(input(f'Digite o {contador}° valor: '))
  if valor % 2 == 0: #Se a divisão do valor digitado for igual a 0,significa que o número e par
    num[0].append(valor)
  else:
    num[1].append(valor)
print('-=' * 30)
num[0].sort() #Ordenando os valores da lista par
num[1].sort() #Ordenando os valores da lista impar
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')
