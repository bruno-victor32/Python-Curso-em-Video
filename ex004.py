#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

nome = input('Digite algo ')
print('O tipo primitivo desse valor é ', type(nome)) #Como eu não fiz a conversão no input,sempre vai mostrar que e do tipo string mesmo sendo numero
print('Só tem espaços?', nome.isspace())
print('É um número?', nome.isnumeric())
print('É alfabético?', nome.isalpha())
print('É alfanumerico?', nome.isalnum())
print('Está em maiúsculas?', nome.isupper())
print('Está em minúsculas', nome.islower())
print('Está capitalizada?', nome.istitle())

#Toda função input retorna sempre uma string independente do tipo