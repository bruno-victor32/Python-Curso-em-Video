''' Crie um programa que leia vários números inteiros pelo teclado.
 O programa só vai parar quando o usuário digitar o valor 999, que é a
  condição de parada. No final, mostre quantos números foram digitados e
   qual foi a soma entre eles (desconsiderando o flag).'''

soma = 0
totalNumeros = 0
num = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]:'))
    totalNumeros = totalNumeros + 1
    soma = soma + num
    if num == 999:
        totalNumeros = totalNumeros -1
        soma = soma - 999
print('Você digitou {} números e a soma entre eles foi {}'.format(totalNumeros,soma))

print('-'*35)

numero = contador = somar = 0 #Dessa forma estou dizendo que numero = 0 , contador = 0, somar = 0
numero = int(input('Digite um número [999 para parar]: '))
while numero != 999:
    somar = somar +numero
    contador = contador + 1
    numero = int(input('Digite um número [999 para parar]: '))#Como já tem um print acima pedindo um número, aqui ele não vai considerar o 999
print('Você digitou {} números e a soma entre eles foi {}.'.format(contador, somar))
