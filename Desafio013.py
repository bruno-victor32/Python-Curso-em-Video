#Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento

salarioAntigo = float(input('Qual é o salário do funcionário? R$'))
aumento = salarioAntigo * 15 / 100
print('Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}'.format(salarioAntigo, (salarioAntigo + aumento)))