'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem
 por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado
 (entre 0 e 20) e mostrá-lo por extenso'''
resp = ' '
contagem = ('Zero', 'Um','Dois', 'Três', 'Quatro','Cinco',
            'Seis', 'Sete', 'Oito','Nove','Dez','Onze',
            'Doze','Treze','Quartoze','Quinze','Dezesseis',
            'Dezessete','Dezoito','Dezenove','Vinte' ) #Aqui e uma tupla
while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if num <= 20 and num >= 0: #if 0 <= num <= 20: #Aqui e uma validação para verificar si o número digitado está dentro do limite
            break
        print('Tente novamente. ',end='')
    print(f'Você digitou o número {contagem[num]}')
    resp = str(input('Você quer continuar:')).strip().upper()[0]
    if resp == 'N':
        break




