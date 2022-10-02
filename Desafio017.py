#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triãngulo retãngulo,
# calcule e mostre o comprimento da hipotenusa

import math
catetoOposto = float(input('Comprimento do cateto oposto: '))
catetoAdjacente = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa vai medir {:.2f}'.format(math.hypot(catetoOposto, catetoAdjacente)))