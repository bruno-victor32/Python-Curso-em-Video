'''Crie um programa que leia dois valores e mostre um menu como o ao lado na tela:
Seu programa deverá realizar a operação solicitada em cada caso.
[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa
'''


opcao = 0
primeiroValor = int(input('Primeiro Valor: '))
segundoValor = int(input('Segundo Valor: '))
while opcao != 5:
    print(' [ 1 ] somar')
    print(' [ 2 ] multiplicar')
    print(' [ 3 ] maior')
    print(' [ 4 ] novos números')
    print(' [ 5 ] sair do programa')
    opcao = int(input('>>>>>>>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = primeiroValor + segundoValor
        print('A soma entre {} + {} é {}'.format(primeiroValor,segundoValor, soma))
        print('=-=' * 10)
    elif opcao == 2:
        multiplicar = primeiroValor * segundoValor
        print('O resultado de {} X {} é {}'.format(primeiroValor,segundoValor,multiplicar))
        print('=-=' * 10)
    elif opcao  == 3:
        if primeiroValor > segundoValor:
            print('Entre {} e {} o maior valor é {}'.format(primeiroValor,segundoValor,primeiroValor))
        elif segundoValor > primeiroValor:
            print('Entre {} e {} o maior valor é {}'.format(primeiroValor,segundoValor,segundoValor))
        else:
            print('São valores iguais')
    elif opcao == 4:
        print('Informe os números novamente: ')
        primeiroValor = int(input('Primeiro valor: '))
        segundoValor = int(input('Segundo valor: '))
        print('=-=' * 10)
    elif opcao == 5:
        print('Finalizado...')
        print('=-=' * 10)
    elif opcao > 5:
        print('Opção inválida. Tente novamente')
        print('=-=' * 10)

print('Fim do programa! Volte sempre!')




