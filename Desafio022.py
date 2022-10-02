#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas.
#O nome com todas minúsculas
#Quantas letras ao todos(sem considerar espaços)
#Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))#Aqui estou subtraindo o total de letras menos a quantidade de espaço, por isso tem "-" no codigo
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()#Estou gerando uma lista de todas as cadeias de caracteres
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0],len(separa[0])))#Aqui vai mostrar o primeiro item da lista em seguida vai contar esse primeiro item da lista