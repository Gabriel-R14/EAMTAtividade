import pygame
import random
from pygame.locals import *

pygame.init()

tela_resolucao = (800, 600)
tela = pygame.display.set_mode(tela_resolucao)
pygame.display.set_caption('Atividade EAMT')

background = pygame.image.load('imagens/fundo.jpg')
background = pygame.transform.scale(background, tela_resolucao)

dave = pygame.image.load('imagens/dave.png')
dave_size = (256.5, 253)
dave = pygame.transform.scale(dave, dave_size)
plataforma = pygame.image.load('imagens/plataforma.png')
plataforma_size = (800, 75)
plataforma = pygame.transform.scale(plataforma, plataforma_size)

x = 300
y = 310
vel = 25

number1 = pygame.image.load('imagens/number1.png')
number2 = pygame.image.load('imagens/number2.png')
number3 = pygame.image.load('imagens/number3.png')
number4 = pygame.image.load('imagens/number4.png')
number5 = pygame.image.load('imagens/number5.png')
number6 = pygame.image.load('imagens/number6.png')
number7 = pygame.image.load('imagens/number7.png')
number8 = pygame.image.load('imagens/number8.png')
number9 = pygame.image.load('imagens/number9.png')
number10 = pygame.image.load('imagens/number10.png')

numeros = (number1, number2, number3, number4, number5, number6, number7, number8, number9, number10)

executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

        tela.blit(dave, (x, y))

        if evento.type == KEYDOWN:
            if evento.key == K_RIGHT:
                x += vel
            if evento.key == K_LEFT:
                x -= vel


    tela.blit(background, (0, 0))
    tela.blit(plataforma, (0, 550))
    tela.blit(dave, (x, y))
    tela.blit(number3, (0, 0))
    pygame.display.flip()