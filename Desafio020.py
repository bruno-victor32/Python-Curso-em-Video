#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle
nome01 = str(input('Primeiro aluno: '))
nome02 = str(input('Segundo aluno: '))
nome03 = str(input('Terceiro aluno: '))
nome04 = str(input('Quarto aluno: '))
alunos = [nome01, nome02, nome03, nome04]
shuffle(alunos)
print('A ordem de apresentação será {}'.format(alunos))
