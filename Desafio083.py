''' Crie um programa onde o usuário digite uma expressão qualquer
que use parênteses. Seu aplicativo deverá analisar se a expressão
passada está com os parênteses abertos e fechados na ordem correta.'''

#Toda string e uma lista também,eu consigo utilizar o for para pegar cada letra ou cada simbolo

expr = str(input('Digite a expressão: '))
pilha = [] #Criando uma lista vazia
for simb in expr: #Para cada simbolo em expressão
    if simb == '(': #Si o simbolo for de um parenteses aberto
        pilha.append('(') #Eu vou colocar ele na pilha,um caractere de parenteses abrindo
    elif simb == ')':
        if len(pilha) > 0: #Si o tamanho da minha pilha for maior que 0,significa que não está vazio
            pilha.pop() #O comando pop retira o ultimo elemento de uma lista
        else: #Si a pilha estiver vazia
            pilha.append(')') # eu coloco um parenteses de fechamento na pilha,significa que teve mais caracteres de fechamento do que abrindo
            break
if len(pilha) == 0: #Si a pilha estiver vazia,ou seja, si o parenteses aberto '(' encontrou o parenteses fechando ')'
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')

#Resolução do exercicio de forma escrita para entender.
#Sempre que eu encontrar um parenteses aberto '('  eu adiciono na lista chamada 'lista'
#Quando eu acho um parenteses fechando ')' eu retiro da pilha um parenteses aberto '('
#E vice-versa
#Caso eu encontre uma pilha vazia eu coloco um parenteses fechando ')' e vou dar break,significando que
#a pilha não está vazia e assim dando um erro