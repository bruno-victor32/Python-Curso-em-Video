#Escreva um programa que converta uma temperatura digitada em ºC e converta para °F

celsius = float(input('Informe a temperatura em ºC: '))
conversao = (celsius * 1.8) + 32
print('A temperatura de {}ºC corresponde a {}°F !'.format(celsius,conversao))