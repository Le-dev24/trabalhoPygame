import pygame
import random

class Objeto:
    def __init__(self):
        self.altura = 50
        self.largura = 50

        self.x = random.randint(0,550)
        self.y = 0

        self.vel = 5

        self.rect = pygame.Rect(self.x, self.y, self.altura, self.largura)

        self.imagem = pygame.image.load('assets/objeto.png')
        self.imagem = pygame.transform.scale(self.imagem, (50, 50))

    def atualizar (self):
        self.y += self.vel

        # voltando para o topo quando sai da tela
        if self.y > 400:
            self.y = 0
            self.x = random.randint(0, 550)

        self.rect.topleft = (self.x, self.y)

    def desenhar(self, tela):
        #pygame.draw.rect(tela, (255, 0, 0), self.rect)
        tela.blit(self.imagem, (self.x, self.y))



