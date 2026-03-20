import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # tamanho
        self.largura = 50
        self.altura = 50

        # velocidade
        self.vel = 5

        # retângulo usado para a colisão
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)

    def mover(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.x -= self.vel
        if teclas[pygame.K_RIGHT]:
            self.x += self.vel

        # limitar dentro da tela
        if self.x < 0:
            self.x = 0
        if self.x > 550:
            self.x = 550

        # atualiza a posição do retângulo
        self.rect.topleft = (self.x, self.y)

    def desenhar(self, tela):
        pygame.draw.rect(tela, (0, 0, 255), self.rect)

