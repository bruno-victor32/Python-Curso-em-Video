''' Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

contador = 1
print('Gerador de PA')
print('=-=' * 10)
primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiroTermo
while contador <= 10:
    print('{} -> '.format(termo), end='')
    contador = contador + 1
    termo = termo + razao
print('FIM')


