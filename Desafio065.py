''' Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi
o maior e o menor valores lidos. O programa deve perguntar ao usuário se
 ele quer ou não continuar a digitar valores.'''

resp = 'S'
quantidadeNumeros = 0
soma = 0
num = 0
media = 0
maior = 0
menor = 0
while resp == 'S':
    quantidadeNumeros = quantidadeNumeros + 1
    num = int(input('Digite um número: '))
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]#Estou jogando a string para maiuscula, retirando o espaço e vou considerar somente a primeira letra
    soma = (soma + num)
    if quantidadeNumeros == 1:#Se o contador for igual a 1
        maior = num #A variavel maior recebe o valor da variavel num
        menor = num #A variavel menor recebe o valor da variavel num
    elif num > maior: #Senão se a variavel num for maior que a variavel maior
        maior = num
    elif num < menor:
        menor = num
media = soma / quantidadeNumeros
print('Você digitou {} números e a média foi {:.1f}'.format(quantidadeNumeros,media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
