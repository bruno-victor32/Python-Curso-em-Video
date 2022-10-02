#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros

metros = float(input('Uma distância em metros: '))
print('A medida de {}m corresponde a\n {}km \n {}hm \n {}dam \n {:.0f}dm \n {:.0f}cm \n {:.0f}mm'.format(metros, (metros / 1000), (metros / 100), (metros / 10),(metros * 10),(metros * 100), (metros * 1000)))