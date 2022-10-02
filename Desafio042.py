#Refaça o DESAFIO 035 dos triãngulos, acrescentando o recurso
# de mostrar que tipo de triângulo será formado:
#Equilátero: todos os lados iguais
#Isosceles: dois lados iguais
#Escaleno: todos os lados diferentes

print('Analisando Triângulos')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento:  '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 and r1 == r3:
        print('Os segmentos acima PODEM FORMAR um triângulo EQUILATERO!')
    elif  r1 == r2 or r1 == r3 or r2 == r3:
        print('Os segmentos acima PODEM FORMAR um triângulo ISOSCELES!')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO!')
else:
    print('Os segmentos acima não podem formar triângulo')