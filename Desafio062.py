'''Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar
mais alguns termos. O programa encerrará quando ele disser que quer mostrar
 0 termos.'''


print('Gerador de PA')
print('=-=' * 10)
primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiroTermo
contador = 1
termosAMais = 10 #Vai iniciar valendo 10 a variavel
total = 0
while termosAMais != 0: #Enquanto termoAMais for diferente de 0 repita
    total = total + termosAMais
    while contador <= total:
        print('{} -> '.format(termo), end='')
        contador = contador + 1
        termo = termo + razao
    print('PAUSA')
    termosAMais = int(input('Quantos termos você quer mostrar a mais?'))
print('Progressão finalizada com {} termos mostrados.'.format(total))