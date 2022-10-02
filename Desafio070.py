'''Crie um programa que leia o nome e o preço de vários produtos.
 O programa deverá perguntar se o usuário vai continuar ou não.
 No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''

print('-' * 30)
print('\tLOJA SUPER BARATÃO\t')
print('-' * 30)
contador = 0
menor = 0
totCompras = 0
totalProdutosCaros = 0
nomeProdutoBarato = 0
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    totCompras = totCompras + preco #Total da compras
    contador = contador + 1
    if contador == 1: #Se for o primeiro produto
        menor = preco
        nomeProdutoBarato = produto
    elif preco < menor:
        menor = preco
        nomeProdutoBarato = produto
    if preco > 1000: #Total de produtos que valem mais de 1000
        totalProdutosCaros = totalProdutosCaros + 1

    resp = ' ' #Utilizo essa variavel em branco para que quando eu digite ela fique com valor e para n deixar o programa aceitar algo diferente de S ou N
    while resp not in 'SN':#Enquanto a resp for diferente de S ou N, NÃO FAÇA
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resp == 'N': #Si caso não queira continuar dá o break
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))#40 caracteres eu vou mostrar um traço e centralizar isso
print(f'O total da compra foi R${totCompras:.2f}')
print(f'Temos {totalProdutosCaros} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeProdutoBarato} que custa  R${menor:.2f}')
