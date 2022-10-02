#Fatiamento:Fatiar uma string e conseguir pegar pedaços dela
#Uma string com seus micro-elementos ela e imutavel

frase = 'Curso em Video Python'
print('Vai mostrar a quarta letra da frase que nesse caso é -{}-'.format(frase[3]))

print('--------------------------------')

print(frase[3:13])

print('--------------------------------')

print(frase[13:])

print('--------------------------------')

print(frase[1:15:2])

print('--------------------------------')

print(frase[::2]) #Dessa maneira eu não sei o inicio e não sei o final,somente sei que vai pular de dois em dois

print('--------------------------------')

#Para imprimir um texto grande eu faço da seguinte maneira

print("""Estamos te enviando este e-mail para te parabenizar pela conquista da sua bolsa de estudos 
no Santander Bootcamp. Você já deu o aceite na sua vaga pelo Becas e agora está oficialmente dentro 
do programa! Wooooww 
Você já pode começar agora a sua jornada de estudos pela trilha do Santander Bootcamp!""")

print('--------------------------------')

print(frase.count('o'))

print('--------------------------------')

print(frase.upper().count('O'))#Pego a frase jogo para maiusculo a frase toda e vejo quantos "O" tem na frase

print('--------------------------------')

#Comando len para ver o tamanho da frase

print(len(frase))

print('--------------------------------')

#comando strip retira os espaços indesejados,como nesse caso o espaço em branco antes de Curso e o espaço em branco depois de Python
fraseComEspaço = '   Curso em Vídeo Python    '
print(len(fraseComEspaço.strip()))

print('--------------------------------')

#O replace só muda,mas ele não salva o resultado da troca
print(frase.replace('Python','Android'))
print(frase)
print('----------------------------------')

#Uma string com seus micro-elementos ela e imutavel,
#a não ser que eu utilize uma função de transformação
# de string nesse caso o "replace" e em seguida eu faça
#uma atribuição
frase01 = frase.replace('Python','Android')
print(frase01)

print('----------------------------------')

print('Curso' in frase)

print('----------------------------------')

print(frase.find('Video'))

print('----------------------------------')

print(frase.lower().find('video'))#Pego a frase jogo para minusculo a frase toda e vejo si tem a palavra "video" na frase

print('----------------------------------')

#Agora vai criar uma lista com o "split",em python as listas são identificadas por []
print(frase.split())

print('----------------------------------')

dividido = frase.split()
print(dividido[0])#Mostrando o primeiro item da lista
print(dividido[1])#Mostrando o segundo item da lista
print(dividido[2])#Mostrando o terceiro item da lista
print(dividido[3])#Mostrando o quarto item da lista

print('----------------------------------')

dividido = frase.split()
print(dividido[2][3])#Mostrando o terceiro item da lista,quero saber/mostrar qual e a letra 3