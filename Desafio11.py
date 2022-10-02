#Faça um programa que leia a largura e a altura de uma parede em metros
#Calcule a sua área e a quantidade de tinta necessaria para pintá-la
#Sabendo que cada litro de tinta,pinta uma  área de 2m²

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
areaQuadrada = largura * altura
tinta = areaQuadrada / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(largura, altura, areaQuadrada))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
