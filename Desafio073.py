'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

times = ('Corinthias', 'Palmeiras', 'Santos', 'Grêmio','Cruzeiro',
         'Flamengo','Vasco','Chapecoense','Atlético', 'Botafogo',
         'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense',
         'Sport Recife','EC Vitória','Coritiba', 'Avaí',
         'Ponte Preta','Atlético-GO')
print('-=-' * 30)
print(f'Lista de times do Brasileirão: {times}')
print('-=-' * 30)
print(f'Os 5 primeiros são {times[:5]}')
print('-=-' * 30)
print(f'Os 4 últimos são {times[-4:]}')
print('-=-' * 30)
print(f'Times em ordem alfabética: { sorted(times)}') #O sorted não muda a ordem da minha tupla,ele vai manter porque a tupla e imutavel.Vai ordenar e mostrar na tela,mas não vai modificar a tupla
print('-=-' * 30)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição ')#Ou usamos o format ou a "" aspas duplas dentro do index.O +1 e por causa que a primeira posição e  0,

print('-=-'  *30)
print('-=-'  *30)
print('-=-'  *30)
#Outra maneira de fazer a lista de times do Brasileirão
for time in times:
    print(f'Os times do brasileirão são {time}')

print('-=-' * 30)
print(f'Os 5 primeiros são {times[0:5]}') #Do 0 a 5 tem 6 times, só que o fatiamento vai ignorar o sexto time
print('-=-' * 30)