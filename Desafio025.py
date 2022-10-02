#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))

print('------------------------------------------')

#Reparei que se um nome tiver "Silva" na escrita, como "SILVANEI", ainda assim ele é validado com o True. Por isso fiz desse jeito:
# 1) Recebo o nome tratado para evitar espaços extras
nome = str(input('Informe seu nome completo: ')).strip()

# 2) Converto o nome para letras maiúsculas, depois
# o divido e guardo a lista em uma nova variável:
divisao = nome.upper().split()

# 3) Agora executo o teste para verificar se existe SILVA em
# alguns dos itens da lista criada.
print('SILVA' in divisao)