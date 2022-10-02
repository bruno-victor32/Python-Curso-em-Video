#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
#preço normal e condição de pagamento:
#á vista dinheiro/cheque:10% de desconto
#á vista no cartão:5% de desconto
#em até  2x no cartão: preço normal
#3x ou mais no cartão:20% de juros

print('========== LOJAS BRUNO ==========')
preco = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    desconto = (preco * 10) / 100
    valorComDesconto = preco - desconto
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco,valorComDesconto))
elif opcao == 2:
    desconto = (preco * 5) / 100
    valorComDesconto = preco - desconto
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco,valorComDesconto))
elif opcao == 3:
    parcelamento = preco / 2
    print('Sua compra será parcelada em 2x de R${:.2f} '.format( parcelamento))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco,preco))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    juros = (preco * 20) / 100
    valorComJuros = preco + juros
    parcelamento = valorComJuros / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas,parcelamento))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco,valorComJuros))