nome = input("Qual é seu nome?")
n1 = int(input('Digite um valor: '))
n2 = int(input( 'Digite outro valor:'))
soma = n1 + n2
multiplicação = n1 * n2
divisao = n1/n2
divisaointeira = n1//n2
potencia = n1**n2
print('Prazer em te conhecer {:=^20}!'.format(nome))
print('A soma é {}, o produto é {} e a divisao é {:.3f}'.format(soma,multiplicação,divisao),end = '')
print(' ,divisão inteira {} e potencia {}'.format(divisaointeira,potencia))