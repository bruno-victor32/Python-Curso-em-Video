#Crie um programa que leia um número inteiro e mostre na tela se ele é Impar ou PAR

num = int(input('Me diga um número qualquer: '))
restoDaDivisao = num % 2
if restoDaDivisao == 0:
    print('O número {} é PAR'.format(num))
else:
    print('O número {} é IMPAR'.format(num))