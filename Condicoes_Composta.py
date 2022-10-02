#Estrutura condicional composta porque tem o else

nome = str(input('Qual e seu nome?'))
if nome == 'Bruno':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia,{}!'.format(nome))