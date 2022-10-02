#Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
#calcule seu IMC e mostre seu status, de acordo com tabela abaixo:
#Abaixo de 18.5:Abaixo do PESO
#Entre 18.5 e 25: PESO IDEAL
#25 até 30:Sobrepeso
#30 até 40:Obesidade
#Acima de 40: Obesidade mórbida

peso = float(input('Qual é seu peso? (kg)'))
altura = float(input('Qual é sua altura? (m)'))
imc = peso / (altura * altura)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif imc >= 18.5 and imc < 25:
    print('PARABÉNS, você esta na faixa de PESO NORMAL')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso')
elif imc >= 30 and imc < 40:
    print('Você está em OBESIDADE')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
