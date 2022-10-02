#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.Faça um programa
#que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

import random
nome01 = str(input('Primeiro aluno: '))
nome02 = str(input('Segundo aluno: '))
nome03 = str(input('Terceiro aluno: '))
nome04 = str(input('Quarto aluno: '))
alunos = [nome01, nome02, nome03, nome04]
print('O aluno escolhido foi {}'.format(random.choice(alunos)))