#Estrutura aninhada no python sempre vai ter um if, e nem sempre vai ter o else ou elif
nome = str(input('Qual é seu nome? '))
if nome == 'Bruno':
    print('Que nome bonito')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo': #O "or" significa "ou".
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Jessica Juliana':  #O "in" significa "igual".O nome e igual a Ana, igual a Claudia, igual a Jessica, igual a Juliana
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia,{}!'.format(nome))