#Faça um programa que calcule a soma entre todos os
#números impares que são múltiplos de três e que se encontram
# no intervalo de 1 até 500

cont = 0 #Geralmente o contador conta mais um
soma = 0 #Acumulador geralmente soma os valores
for contador in range(1,501, 2):
    if contador % 3 == 0: #Descobrir os números que são multiplos de 3
        soma = soma + contador
        cont = cont + 1 #Contagem dos números que são multiplos de três
print('A soma de todos os {} valores solicitados é {}'.format(cont,soma))

