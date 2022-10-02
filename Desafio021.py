#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3

import pygame

# Inicializando o mixer PyGame
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()

pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()

#Para quem não está conseguindo reproduzir
# ou precisou colocar um input(), o Pygame
# mudou um pouco desde a postagem do vídeo,
# agora é necessário iniciar o mixer e o pygame,
# além disso, como os comandos do mixer vem primeiro
# que o wait(), o mixer deve ser inicializado primeiro,
# podem testar e mudar a ordem dos inicializadores para
# comprovarem que não funciona. Essa é uma das formas corretas,
# mas colocar o input() não é legal pois força o programa a esperar
# que você insira algum valor manualmente, não encerrando o programa ao final da reprodução.