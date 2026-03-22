import pygame

from code.player import Player
from code.objeto import Objeto
from code.menu import Menu

class Game:
    def __init__(self):
        # tamanho da tela
        self.largura = 600
        self.altura = 400

        # criar janela
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption('UFO Run')

        self.bg = pygame.image.load('assets/background.png')
        self.bg = pygame.transform.scale(self.bg, (600, 400))

        # controle de tempo
        self.clock = pygame.time.Clock()

        # controle de jogo
        self.rodando = True

        # objetos do jogo
        self.player = Player(250, 350)
        self.objeto = Objeto()

        # menu
        self.estado = 'menu'
        self.menu = Menu(self.tela)

    def resetar_jogo(self):
        self.player.x = 250
        self.player.y = 250
        self.player.rect.topleft = (self.player.x, self.player.y)

        self.player.x = self.player.x_inicial
        self.player.y = self.player.y_inicial
        self.player.rect.topleft = (self.player.x, self.player.y)

        import random
        self.objeto.x = 0
        self.objeto.y = random.randint(0, 550)
        self.objeto.rect.topleft = (self.objeto.x, self.objeto.y)

    def run(self):
        while self.rodando:
            self.clock.tick(60)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.rodando = False

                if evento.type == pygame.KEYDOWN:
                    if self.estado == 'menu' and evento.key == pygame.K_SPACE:
                        self.estado = 'jogando'

                    if self.estado == 'game_over' and evento.key == pygame.K_r:
                        self.resetar_jogo()
                        self.estado = 'jogando'

            # menu

            if self.estado == 'menu':
                self.menu.desenhar()
                pygame.display.update()


            # estado: jogando
            if self.estado == 'jogando':
                teclas = pygame.key.get_pressed()
                self.player.mover(teclas)

                self.objeto.atualizar()

                #colisão
                if self.player.rect.colliderect(self.objeto.rect):
                    self.estado = 'game_over'

                #self.tela.fill((0, 0, 0))
                self.tela.blit(self.bg, (0, 0))

                self.player.desenhar(self.tela)
                self.objeto.desenhar(self.tela)

                pygame.display.update()

            # estado: game over
            elif self.estado == 'game_over':
                self.tela.blit(self.bg, (0, 0))

                fonte_titulo = pygame.font.SysFont(None, 60)
                fonte_texto = pygame.font.SysFont(None, 35)

                texto = fonte_titulo.render('GAME OVER',True, (255, 0, 0))
                reiniciar = fonte_texto.render('Pressione R para jogar novamente', True, (255, 255, 255))

                # centralizar
                texto_rect = texto.get_rect(center=(self.largura // 2, 150))
                reiniciar_rect = reiniciar.get_rect(center=(self.largura // 2, 230))

                self.tela.blit(texto, texto_rect)
                self.tela.blit(reiniciar, reiniciar_rect)



                pygame.display.update()