import pygame

class Menu:
    def __init__(self, tela):
        self.tela = tela
        self.fonte = pygame.font.SysFont(None, 40)
        self.largura = self.tela.get_width()
        self.altura = self.tela.get_height()
        self.bg = pygame.image.load('assets/background.png')
        self.bg = pygame.transform.scale(self.bg, (self.largura, self.altura))

    def desenhar(self):
        self.tela.blit(self.bg, (0, 0))

        titulo = self.fonte.render('UFO Run', True, (255, 255, 255))
        instrucao = self.fonte.render('Use as setas para mover', True, (200, 200, 200))
        iniciar = self.fonte.render('Pressione espaço para começar', True, (156, 228, 92))

        # centralizar
        titulo_rect = titulo.get_rect(center=(self.largura // 2, 100))
        instrucao_rect = instrucao.get_rect(center=(self.largura // 2, 180))
        iniciar_rect = iniciar.get_rect(center=(self.largura // 2, 260))

        # desenhar
        self.tela.blit(titulo, titulo_rect)
        self.tela.blit(instrucao, instrucao_rect)
        self.tela.blit(iniciar, iniciar_rect)
