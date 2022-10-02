#Faça um programa que leia um ãngulo qualquer e mostre na tela o valor do seno,cosseno e tangente desse ângulo

import math
angulo = float(input('Digite o ângulo que você deseja: '))
anguloRadiano = math.radians(angulo)#Aqui estou convertendo o angulo que foi dado em grau para radianos
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo,math.sin(anguloRadiano)))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo,math.cos(anguloRadiano)))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(angulo,math.tan(anguloRadiano)))