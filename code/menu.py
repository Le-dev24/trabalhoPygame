import pygame

class Menu:
    def __init__(self, tela):
        self.tela = tela
        self.fonte = pygame.font.SysFont(None, 40)

    def desenhar(self):
        self.tela.fill((0, 0, 0))

        titulo = self.fonte.render('Desvie dos Objetos', True, (255, 255, 255))
        instrucao = self.fonte.render('Setas para mover', True, (255, 255, 255))
        iniciar = self.fonte.render('Pressione espaço para começar', True, (255, 255, 0))

        self.tela.blit(titulo, (150, 100))
        self.tela.blit(instrucao, (180, 150))
        self.tela.blit(iniciar, (100, 200))
