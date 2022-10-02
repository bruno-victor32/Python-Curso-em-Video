'''Crie um programa que leia nome e duas notas de vários alunos
 e guarde tudo em uma lista composta. No final, mostre um boletim
 contendo a média de cada um e permita que o usuário possa mostrar
 as notas de cada aluno individualmente.'''

ficha = list() #Criando uma ficha padrão para cada aluno, essa ficha vai ser uma lista
while True: #Criando um looping infinito
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2 # Calculando a media
    ficha.append([nome, [nota1, nota2], media]) #Aqui estou fazendo uma lista composta para os dados do aluno
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn': # Se a resposta digitada for igual a "N" ou "n"
        break #Para o looping
#Estrutura para mostrar o boletim do estudante
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')# Vai mostrar o número "NO" formatado com 4 caracteres alinhados a esquerda
print('-' * 26)
#Para mostrar os dados
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')#Para mostrar o numero eu vou colocar o indice "i".Vou mostrar o nome que e o aluno na posição "0".Vou mostrar a media na posição 2, que vai ser uma casa decimal
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1: #Por exemplo si eu cadastrei o aluno 0 ,1 e aluno 2,então ele tem que ser menos que len ficha ou seja,que e a quantidade de alunos cadastrados meno 1.Por que o primeiro aluno e 0 ultimo e n-1
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}') #opc e a variavel de que aluno ele é,0 e o nome do aluno
print('<<< VOLTE SEMPRE >>>')