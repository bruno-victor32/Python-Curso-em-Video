''' Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
adicionado. No final, serão exibidos todos os valores únicos digitados, em
ordem crescente.'''

valoresDaLista = [] #Criando uma lista
while True: #Enquanto verdadeiro
    valoresDigitados = int(input('Digite um valor: ')) #Digite um valor
    if valoresDigitados not in valoresDaLista: #Se valorDigitado não existe na lista
        valoresDaLista.append(valoresDigitados) #Adicione o valor a lista
        print('Valor adicionado com sucesso...')
    else: #Senao
        print('Valor duplicado! Não vou adicionar...')
    decisao = str(input('Quer continuar? [S/N] ')).upper() #A resposta vai ser convertida em maiuscula
    if decisao == 'N': #Se a resposta for "N"
        break #Termina o programa
    else: #senão
        if decisao != 'S': #Se a resposta for diferente de "S"
            print('Digitou incorretamente,tente novamente')
            decisao = str(input('Quer continuar? [S/N] ')).upper() #Peça novamente uma resposta

print('-=-' * 30)
valoresDaLista.sort() #Colocando os valores da lista em ordem
print(f'Você digitou os valores {valoresDaLista}')

