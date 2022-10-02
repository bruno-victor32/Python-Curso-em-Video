'''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('=' * 30)
print('{:^30}'.format('BANCO CEV')) #TEXTO COM 30 CARACTERES FORMATADOS
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor #Aqui e o montante.Desse montante eu vou ver si dá para tirar 50 reais, quantas vezes forem necessarias
cedulaAtual = 50
totalCedulas = 0
while True: #Enquanto for verdade,vai ser feito até acabar o valor "dinheiro"
    if total >= cedulaAtual: #Si o total atual for maior ou igual ao valor da cedula
        total = total - cedulaAtual
        totalCedulas = totalCedulas + 1
        #Com esse codigo acima eu vou verificar, quantas vezes eu consigo retirar 50 do total
    else:
        if totalCedulas > 0:
            print(f'Total de {totalCedulas} cédulas de R${cedulaAtual}')
        if cedulaAtual == 50: #Aqui e sinal que eu não posso mais tirar 50, eu não conseguir tirar 50 do valor
            cedulaAtual = 20 #Proxima cedula vai virar uma de 20
        elif cedulaAtual == 20:
            cedulaAtual = 10
        elif cedulaAtual == 10:
            cedulaAtual = 1
        totalCedulas = 0
        if total == 0: #Vai parar quando o total for igual a 0,si eu não estiver devendo mais nada
            break
print('-' * 30)
print('Volte sempre ao BANCO CURSO EM VIDEO!Tenha um bom dia')