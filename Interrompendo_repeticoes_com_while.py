cont = 1
while cont <= 10:
    print(cont, '-> ', end='')
    cont = cont + 1
print('Acabou')

print('=' * 35)
print('=' * 35)

#O programa só vai parar quando for digitado "999"
#Isso e uma repetição com o enquanto utilizando "flags"
n = 0
while n != 999:
    n = int(input('Digite um número: '))

print('=' * 35)
print('=' * 35)

n = 0
s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break #Sai do enquanto
    s = s + n #Ele vai sair sem somar, a soma só vai acontecer si não for 999
print('A soma vale {}'.format(s))

print('=' * 35)
print('=' * 35)

#Atualização do python,utilizando fstring

nome = 'José'
idade = 33
print(f'O {nome} tem {idade} anos') #PYTHON 3.6+
print('O {} tem {} anos'.format(nome, idade)) #PYTHON 3

print('=' * 35)
print('=' * 35)

nome1 = 'José'
idade1 = 33
salario = 987.3
print(f'O {nome1:-^20} tem {idade1:->20} anos e ganha R${salario:.2f}')



