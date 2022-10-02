'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
 Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

palavras = ('aprender', 'programar', 'linguagem','python',
            'curso','gratis', 'estudar', 'praticar',
            'trabalhar','mercado', 'programar','futuro')

for p in palavras: #for para cada palavras
    print(f'\nNa palavra {p.upper()} temos:',end='')
    for letra in p: #Para cada letra na palavra "p" eu posso verificar
        if letra.lower() in 'aeiou': #se a letra jogada para minusculo for aeiou
            print(letra, end=' ')