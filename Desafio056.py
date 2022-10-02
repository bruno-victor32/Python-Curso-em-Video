'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.No final do programa,mostre:
A média de idade do grupo
Qual é o nome do homem mais velho
Quantas mulheres têm menos de 20 anos'''

somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''#Vai ficar com o nome vazio no inicio
totMulher20 = 0

for contador in range(1,5):
    print('----- {}ª PESSOA -----'.format(contador))
    nome = str(input('Nome: ')).strip() #Estou utilizando o strip para retirar os espaços
    idade = int(input('Idade: '))
    sexo = str(input('SEXO [M/F]: ')).strip()
    somaIdade = somaIdade + idade
    if contador == 1 and sexo in 'Mm': # sexo in "Mm", significa se o sexo for M ou m
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20: # Se sexo for igual a f ou F e idade for menor que 20 anos
        totMulher20 = totMulher20 + 1

mediaIdade = somaIdade / 4
print('A média de idade do grupo é de {} anos'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maiorIdadeHomem, nomeVelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totMulher20))
