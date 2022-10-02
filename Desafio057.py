'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os
os valores 'M' ou 'F'.Caso esteja errado, peça a digitação novamente
até ter um valor correto'''

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0] #Aqui estou tirando os espaços e deixando tudo em maiusculo e em seguida estou pegando somente a primeira letra
while sexo not in 'MmFf': #Enquanto o sexo não estiver em masculino "M" ,"m" ou feminino "F","f"
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
