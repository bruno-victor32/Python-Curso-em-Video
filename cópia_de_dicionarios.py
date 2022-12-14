# -*- coding: utf-8 -*-
"""Cópia de DICIONARIOS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QzHEyeBG263vUCaaZ-twCExha0w7BZIo

Primeiro Exemplo:
"""

pessoas = {'nome': 'Gustavo','sexo': 'M', 'idade': 22} #Criando um dicionário
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')#Nesse caso e necessario utilizar aspas duplas ""
print(pessoas.keys())#Utilizando chaves "keys" vai retornar nome,sexo e idade
print(pessoas.values())# Utilizando valores "values" vai retornar "Gustavo","M","22" 
print(pessoas.items())

"""Outro exemplo"""

#Acessando chaves,valores e os itens por laço
pessoas = {'nome': 'Gustavo','sexo': 'M', 'idade': 22} #Criando um dicionário
for k in pessoas.keys(): #For para cada key (chave) pessoas.keys
  print(k)

"""Outro exemplo"""

pessoas = {'nome': 'Gustavo','sexo': 'M', 'idade': 22} #Criando um dicionário
for v in pessoas.values():
  print(v)

"""Outro exemplo"""

#Para utilizar items(item) eu vou ter que colocar a chave e o valor
pessoas = {'nome': 'Gustavo','sexo': 'M', 'idade': 22} #Criando um dicionário
for k, v in pessoas.items():
  print(f' {k} = {v}')

"""No dicionario utiliza o "for(laço)" não pode utilizar o "enumerate".Somente utiliza o enumerate em "listas" e "tuplas""""

pessoas = {'nome': 'Gustavo','sexo': 'M', 'idade': 22} #Criando um dicionário
del pessoas['sexo'] #Apagando o sexo
print(pessoas)

"""Outro exemplo"""

pessoas = {'nome': 'Gustavo','sexo': 'M', 'idade': 22} #Criando um dicionário
pessoas['nome'] = 'Leandro' #O nome vai deixar de ser Gustavo e vai mudar para Leandro
print(pessoas)

"""Outro exemplo"""

pessoas = {'nome': 'Gustavo','sexo': 'M', 'idade': 22} #Criando um dicionário
pessoas['peso'] = 98.5 #Adicionando um elemento
print(pessoas)

"""Outro exemplo
Criando um dicionario dentro de uma lista
"""

brasil = [] #Criando uma lista chamada Brasil
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'} #Criando o primeiro dicionário
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'} #Criando o segundo dicionário
brasil.append(estado1) #Adicionado o dicionario "estado1" na lista "Brasil"
brasil.append(estado2) #Adicionado o dicionario "estado2" na lista "Brasil"

print(estado1)
print(estado2) #Vai mostrar somente a lista
print(brasil) #Vai mostrar a lista com os dicionarios
print(brasil[0]) #Vai adentrar dentro da lista e do dicionario e pegar o estado de indice 0 que é o Rio de Janeiro
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

"""Outro exemplo"""

estado = dict() #Criando um dicionario
brasil = list() #Criando uma lista
for contador in range(0, 3):
  estado ['uf'] = str(input('Unidade Federativa:')) #Estou perguntando e colocando a resposta diretamente ao "dicionario" ESTADO
  estado['sigla'] = str(input('Sigla do Estado:'))
  brasil.append(estado.copy()) #Aqui estou fazendo uma copia do dicionario e colocando na lista estado
for e in brasil: #Para cada estado no brasil, Esse for e da lista
  print(e)

print(brasil)

"""Outro exemplo"""

estado = dict() #Criando um dicionario
brasil = list() #Criando uma lista
for contador in range(0, 3):
  estado ['uf'] = str(input('Unidade Federativa:')) #Estou perguntando e colocando a resposta diretamente ao "dicionario" ESTADO
  estado['sigla'] = str(input('Sigla do Estado:'))
  brasil.append(estado.copy()) #Aqui estou fazendo uma copia do dicionario e colocando na lista estado
for e in brasil: #Para cada estado no brasil, Esse for e da lista
  for k, v in e.items(): #For "keys" chaves "value" valores em "e " que foi gerado.Esse for e do dicionario
    print(f'O campo {k} tem valor {v}')

"""Outro exemplo"""

estado = dict() #Criando um dicionario
brasil = list() #Criando uma lista
for contador in range(0, 3):
  estado ['uf'] = str(input('Unidade Federativa:')) #Estou perguntando e colocando a resposta diretamente ao "dicionario" ESTADO
  estado['sigla'] = str(input('Sigla do Estado:'))
  brasil.append(estado.copy()) #Aqui estou fazendo uma copia do dicionario e colocando na lista estado
for e in brasil: #Para cada estado no brasil, Esse for e da lista
  for v in e.values(): #For "keys" chaves "value" valores em "e " que foi gerado.Esse for e do dicionario
    print(f'{v} ',end='')
  print() #Para pular uma linha