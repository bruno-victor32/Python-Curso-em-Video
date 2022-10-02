#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a ultima vez

nome = str(input('Digite uma frase: ')).strip().lower()
print('A letra A aparece {} vezes na frase.'.format(nome.count('a')))
print('A primeira letra A apareceu na posição {}'.format(nome.find('a') + 1))#Para o python a primeira posição e a letra na posição ou indice 0,já para a gente ser humano a primeira posição ou indice e 1,ou seja, a letra na posição1, o +1 e para a contagem iniciar do 1
print('A ultima letra A apareceu na posição {}'.format(nome.rfind('a') + 1))#Em vez de find eu vou usar o rfind,que quer dizer procure a partir do lado direito