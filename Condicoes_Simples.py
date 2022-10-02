#Estrutura condicional simples porque não tem o else

nome = str(input('Qual é seu nome? '))
if nome == 'Bruno':     #Chamamos isso de condição simples porque não tem o else
    print('Que nome bonito!')
print('Tenha um bom dia, {}!'.format(nome))

print('-------------------------------------------------------------------------')
##Estrutura condicional composta porque tem o else

nome = str(input('Qual é seu nome? '))
if nome == 'Bruno':     #Chamamos isso de condição simples porque não tem o else
    print('Que nome bonito!')
else:
    print('Seu nome é tão normal!')
print('Tenha um bom dia, {}!'.format(nome))

print('-------------------------------------------------------------------------')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS !')

print('-------------------------------------------------------------------------')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
print('Parabéns ' if m>=6 else 'Estude mais!')