#Para escrever em vermelho
print('\033[31m Olá,Mundo!')

#Para escrever em vermelho, com fundo amarelo
print('\033[31;43m Olá,Mundo!')

#Para escrever em negrito,com a cor do texto em vermelho e com fundo amarelo
print('\033[1;31;43m Olá,Mundo!')

#Para escrever em negrito,com a cor do texto em vermelho e com fundo amarelo
#Eu não quero que a linha toda fique amarela, somente aonde esta digitado
print('\033[1;31;43m Olá,Mundo!\033[m')

#Para escrever com sublinhado, letra branca e fundo lilas
print("\033[4;30;45m Olá, Mundo!\033[m")

#Para fazer com letra branca e fundo preto
print('\033[30m Olá,Mundo!\033[m')

#Para fazer com letra preta e fundo branco
print('\033[7;30m Olá,Mundo!\033[m')

#Vou fazer sem style, cor do texto amarelo e fundo azul
print('\033[0;33;44m Olá,Mundo!\033[m')

#Caso eu faça igual o de cima e troque somente o 0 por 7, vai inverter
#vai ficar letra azul e fundo amarelo
print('\033[7;33;44m Olá,Mundo!\033[m')

print('=-= '* 20)

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a,b))

print('=-= '* 20)

#Aqui estou usando o format para colocar a cor do inicio, a variavel que eu
#vou mostrar e a cor de fim
nome = 'Guanabara'
print('Olá!Muito prazer em te conhecer,{}{}{}!!!'.format('\033[4;34m',nome,'\033[m'))

print('=-= '* 20)

nome = 'Bruno'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá!Muito prazer em te conhecer,{}{}{}!!'.format(cores['pretoebranco'],nome,cores['limpa']))