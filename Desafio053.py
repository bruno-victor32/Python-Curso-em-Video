#Crie um programa que leia uma frase qualquer e diga se ela é um polindromo, desconsiderando os espaços.
#Ex: Apos a Sopa

frase = str(input('Digite uma frase: ')).strip().upper() #tirando o espaço das frases da frente e atras e já colocando elas em letras maiuscula
palavras = frase.split() #Aqui estou dividindo as palavras,retirando os espaços que tem no meio das palavras.Aqui estou separando em um vetor
junto = ''.join(palavras)#Vai juntar todas as palavras sem espaço.Aqui eu juntei tudo em uma string
inverso = ''
for letra in range(len(junto) - 1, - 1, -1): #Vai pegar o número de letras do junto.Si tiver 20 letras a contagem não vai ser do 0 ao 20 e sim do 0 ao 19, nesse caso ele vai começar do 19, vai até a letra -1 que é a letra depois do 0 e vai voltando uma letra
    inverso = inverso + junto[letra]
print('O inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('Temos um palìndromo!')
else:
    print('A frase digitada não é um palìndromo')

print('-=-' * 10)

frase = str(input('Digite uma frase: ')).strip().upper() #tirando o espaço das frases da frente e atras e já colocando elas em letras maiuscula
palavras = frase.split() #Aqui estou dividindo as palavras,retirando os espaços que tem no meio das palavras.Aqui estou separando em um vetor
junto = ''.join(palavras)#Vai juntar todas as palavras sem espaço.Aqui eu juntei tudo em uma string
inverso = ''
inverso = junto[::-1] #Utilizando o fatiamento
print('O inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('Temos um palìndromo!')
else:
    print('A frase digitada não é um palìndromo')