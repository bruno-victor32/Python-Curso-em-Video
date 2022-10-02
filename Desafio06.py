#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n1 = int(input('Digite um número: '))
dobro = n1 * 2
triplo = n1 * 3
raizQuadrada = n1 **0.5
print('O dobro de {} vale {}'.format(n1,dobro))
print('O triplo de {} vale {}'.format(n1,triplo))
print('A raiz quadrada de {} é igual a {:.2f}.'.format(n1,raizQuadrada))

print('----------------------------------------------------------------')
#Outra maneira de fazer o exercicio
print('O dobro de {} vale {}'.format(n1, (n1 * 2)))
print('O triplo de {} vale {}.\nA raiz quadrada de {} é igual a {:.2f}'.format(n1, (n1*3), n1, pow(n1,(1/2))))