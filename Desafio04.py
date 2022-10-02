#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

n1 = input('Digite um valor: ')
print(type(n1))
print('O valor digitado', n1, 'e inteiro = ',n1.isnumeric())
print('O valor digitado', n1, 'e letra = ',n1.isalpha())
print('O valor digitado', n1, 'e alfanumerico ou letra = ',n1.isalnum())
print('o valor digitado', n1, 'tem todas letras maiusculas =',n1.isupper())