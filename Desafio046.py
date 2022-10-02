#Faça um programa que mostre na tela uma contagem regressiva
#para o estouro de fogos de artifício, indo de 10 até 0, com uma
#pausa de 1 segundo entre eles

from time import sleep
for contador in range(10, -1, -1): # COLOCO -1 PARA ELE CHEGAR NO 0, E O OUTRO -1 E PARA IR TIRANDO UM DA CONTAGEM
    print(contador)
    sleep(1)  # Faz o programa dar um delay
print('BUM! BUM! POOOW!')