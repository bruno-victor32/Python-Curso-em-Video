#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

n1 = int(input('Digite um número: '))
sucessor = n1 + 1
antecessor = n1 - 1
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n1, antecessor, sucessor))

#Outra maneira de fazer o mesmo calculo
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n1, (n1 - 1), (n1 + 1)))