contador = 1 #Contador inicia valendo 1
while contador < 10: #Enquanto contador menor que 10
    print(contador) #Mostre o valor de contador na tela
    contador = contador + 1 # somar mais um no contador
print('Fim')

print('-=-' * 10)
print('-=-' * 10)

n = 1
while n != 0: # enquanto não for digitado o numero 0 será solicitado um valor
    n = int(input('Digite um valor: '))
print('Fim')

print('-=-' * 10)
print('-=-' * 10)

resposta = 'S' #A resposta vai iniciar valendo S
while resposta == 'S': #enquanto a resposta continuar valendo S continue
    n = int(input('Digite um valor: '))
    resposta = str(input('Quer continuar? [S/N] ')).upper()#Estou jogando a resposta para maiusculo,mesmo que eu digite em minusculo
print('Fim')

print('-=-' * 10)
print('-=-' * 10)

numero = 1
while numero != 0: #Enquanto não for digitado o numero 0 será realizado a leitura de um valor
    numero = int(input('Digite um valor: '))
print('Acabou')

print('-=-' * 10)
print('-=-' * 10)

par = 0
impar = 0
numero = 1
while numero != 0: #Enquanto não for digitado o numero 0 será realizado a leitura de um valor
    numero = int(input('Digite um valor: '))
    if numero % 2 == 0:
        par += 1
    else:
        impar +=1
print('Você digitou {} números pares e {} numeros impares'.format(par,impar))
