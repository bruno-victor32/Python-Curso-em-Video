#Desenvolva um programa que pergunte a distância de uma viagem em KM.
#Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200km
# e R$0,45 para viagens mais longes

distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}Km'.format(distancia))
if distancia <= 200:
    precoDistanciaCurta = distancia * 0.50
    print('E o preço da sua passagem será de {:.2f}'.format(precoDistanciaCurta))
else:
    precoDistanciaLonga = distancia * 0.45
    print('E o preço da sua passagem será de R${:.2f}'.format(precoDistanciaLonga))


