'''Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário. No final,
mostre o conteúdo da estrutura na tela.'''

dados = dict() #Criando um dicionario chamado "dados"
dados['nome'] = str(input('Nome: '))
dados['média'] = float(input(f'Média de {dados["nome"]}: '))
print(f'Nome é igual a {dados["nome"]}')
print(f'Média é igual {dados["média"]}')
if dados['média'] >= 7:
    print('Situação é igual a APROVADO')
else:
    print('Situação é igual a REPROVADO')


print('-=' * 30)
print('-=' * 30)
print('RESOLUÇÃO DO PROFESSOR ABAIXO')
print('-=' * 30)
print('-=' * 30)

aluno = dict() #Criando um dicionário
aluno['nome'] = str(input('Nome: ')) #Estou adicionando o nome digitado ao dicionario aluno
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7: #Si a media do aluno estiver abaixo de 7 e acima de 5
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-' * 30)
for k, v in aluno.items(): #Para cada chave e valor in
    print(f' - {k} é igual a {v}')
