'''Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,mostrando no final quantos palpites
foram necessários para vencer '''

from random import randint #Importando somente a função randint
valorSorteado = randint(0,10)
sorteio = 1
palpites1 = 0
print('Sou seu computador...Acabei de pensar em um número entre 0 e 10. ')
print('Será que você consegue adivinhar qual foi?')

while sorteio != valorSorteado:
      sorteio = int(input('Qual é seu palpite? '))
      palpites1 = palpites1 + 1
      if sorteio == valorSorteado:
          print('Acertou com {} tentativas. Parabéns!'.format(palpites1))
      elif sorteio != valorSorteado:
          print('Menos... Tente mais uma vez')


print('=-= ' * 10 + 'Resolução do Prof' + ' =-= ' * 10 )

from random import randint #Importando somente a função randint
computador = randint(0,10)
print('Sou seu computador...Acabei de pensar em um número entre 0 e 10. ')
print('Será que você consegue adivinhar qual foi?')
acertou = False #Vai iniciar valendo false porque eu não acertei ainda
palpites = 0
while not acertou: #Enquanto não acertar
    jogador = int(input('Qual é seu palpite? '))
    palpites = palpites + 1
    if jogador == computador: #Si o numero sorteado pelo PC for igual ao numero que o usuario digitou
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez.')
        elif jogador > computador:
            print('Menos...Tente mais uma vez')
print('Acertou com {} tentativas.Parabéns'.format(palpites))
