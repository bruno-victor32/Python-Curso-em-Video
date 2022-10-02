'''Faça um programa que leia o peso de cinco pessoas.No final, mostre qual foi o maior e o menor peso lidos'''

maior = 0
menor = 0
for contador in range(1,6):
    peso = float(input('Peso da {}ª pessoa:'.format(contador)))
    if contador == 1:#Se for o primeiro peso, ele vai ser o maior e o menor peso
         maior = peso
         menor = peso
    else:
        if peso > maior:#A partir do segundo peso digitado ele vai começar a contabilizar
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}kg'.format(maior))
print('O menor peso lido foi de {}kg'.format(menor))