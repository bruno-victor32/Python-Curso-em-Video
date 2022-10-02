#Refaça o DESAFIO 009 ,mostrando a tabuada de um número que o usuário
#escolher, só que agora utilizando um laço for

num = int(input('Digite um número para ver sua tabuada: '))
for contador in range(0,11):
    contagem = contador * num
    print('{} x {} = {}'.format(num,contador,contagem))
