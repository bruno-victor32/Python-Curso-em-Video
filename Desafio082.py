'''Crie um programa que vai ler vários números e colocar em uma lista.
 Depois disso, crie duas listas extras que vão conter apenas os valores
 pares e os valores ímpares digitados, respectivamente. Ao final, mostre
 o conteúdo das três listas geradas.'''

listaCompleta = []
listaPar = []
listaImpar = []

while True:
    num = int(input('Digite um número: '))
    listaCompleta.append(num)
    if num % 2 == 0:
        listaPar.append(num)
    else:
        listaImpar.append(num)
    decisao = str(input('Quer continuar? [S/N]')).upper()
    if decisao == 'N':
        break
    else:
        if decisao != 'S':
            print('Digite novamente...Resposta invalida')
            decisao = str(input('Quer continuar? [S/N]')).upper()



print('-=' * 30)
print(f'A lista completa é {listaCompleta}')
print(f'A lista de pares é {listaPar}')
print(f'A lista de ímpares é {listaImpar}')
