#Escreva um programa que pergunte o salário de um funcionário
#e calcule o valor do seu aumento.Para salários superiores a
#R$1250,00, calcule um aumento de 10%.Para os inferiores ou
#iguais, o aumento é de 15%

sal = float(input('Qual é o salário do funciomário? R$'))
if sal > 1250:
    aumento = (sal * 10)/100
    salNovo = sal + aumento
else:
    aumento = (sal * 15)/100
    salNovo = sal + aumento

print('Quem ganhva R${:.2f} passa a ganhar R${:.2f} agora'.format(sal,salNovo))