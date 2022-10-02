''' Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário
quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''

totPessoas = 0
totMasculino = 0
totFeminino = 0
while True:
    print('-' * 30)
    print('\t CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF': #Enquanto o usuario não digitar masculino ou feminino eu não vou deixar passar
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0] #Pegando somente a primeira letra
    print('-' * 30)
    if idade >= 18:
        totPessoas = totPessoas + 1
    if sexo == 'M':
        totMasculino = totMasculino + 1
    if idade < 20 and sexo == 'F':
        totFeminino = totFeminino + 1
    resp = ' '
    while resp not in 'SN': #Enquanto o usuario não digitar SIM ou NÃO eu não vou deixar passar
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {totPessoas}')
print(f'Ao todo temos {totMasculino} homens cadastrados')
print(f'E temos {totFeminino} mulheres com menos de 20 anos')