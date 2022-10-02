#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.No final mostre os 10
#primeiros termos dessa progreção

print('=' * 30)
print ('\t 10 TERMOS DE UMA PA \t\t\t')
print('=' * 30)
PrimTermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = PrimTermo + (10 - 1) * razao #formula de uma PA, para ter 10 termos
for contador in range(PrimTermo, decimo + razao ,razao ):
    print('{}'.format(contador),end= ' -> ')
print('ACABOU')