#Desenvolva um programa que leia as duas notas de um aluno,calcule e mostre a sua média

nota01 = float(input('Primeira nota do aluno: '))
nota02 = float(input('Segunda nota do aluno: '))
media = (nota01 + nota02) / 2
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(nota01, nota02, media))
