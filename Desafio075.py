'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
em uma tupla. No final, mostre:'''

tupla = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')),
         int(input('Digite o último número: ')))

print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla: #Si o valor 3 estiver dentro da tupla
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição') #Mostra a posição
else:#Senao
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in tupla: #Para cada numero "n" em tupla eu faço
    if n % 2 == 0: #Verificando si o numero e divisivel por 2
        print(f'{n}  ', end='')



