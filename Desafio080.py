'''Crie um programa onde o usuário possa digitar cinco valores numéricos
 e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
  No final, mostre a lista ordenada na tela.'''

lista = [] #Criando uma lista vazia
for contador in range(0, 5): #Vai lêr 5 valores
    n = int(input('Digite um valor: '))
    if contador == 0: #Si for o primeiro valor digitado
        lista.append(n) #Adicione esse valor a lista
        print('Adicionado ao final da lista')
    elif n > lista[len(lista)-1]:# Posso tbm fazer assim 'lista[-1]' #Senão Se o numero digitado "n" for maior que o ultimo valor adicionado na lista
        lista.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista): #Vai da posição 0 até a ultima posição
            if n <= lista[pos]: #Eu vou verificar dentro de cada posição, si o numero que eu quero inserir e menor igual a ele.Si for menor igual eu vou inserir em uma posição especifica
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos}')
                break
            pos = pos + 1 #pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')