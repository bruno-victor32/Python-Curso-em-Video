#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

print('======== Empréstimo Bancário ========' )
print('=====================================')
casa = float(input('Digite o valor da casa? R$'))
salario = float(input('Digite o salário do comprador? R$'))
anos = int(input('Deseja pagar em quantos anos? R$'))
conversao_anos_meses = anos * 12
prestacao = casa / conversao_anos_meses
porcentagem = ((salario *30)/100)
print('Para pagar uma casa de {:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, anos, prestacao))
if prestacao > porcentagem :
    print('Não é possível fazer o emprestimo devido a prestação mensal exceder 30% do salario')
else:
    print('Será concedido o emprestimo')