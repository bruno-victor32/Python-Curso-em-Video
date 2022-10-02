try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except:
    print('Infelizmente tivemos um programa :(')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte sempre! Muito Obrigado')