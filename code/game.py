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
        pygame.display.set_caption('Desvie dos objetos')

        self.bg = pygame.image.load('assets/background.png')
        self.bg = pygame.transform.scale(self.bg, (600, 400))

        # controle de tempo
        self.clock = pygame.time.Clock()

        # controle de jogo
        self.rodando = True

        # estado do jogo
        self.estado = 'jogando'

        # objetos do jogo
        self.player = Player(250, 350)
        self.objeto = Objeto()

        # menu
        self.estado = 'menu'
        self.menu = Menu(self.tela)

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
                self.tela.fill((0, 0, 0))

                fonte = pygame.font.SysFont(None, 50)
                texto = fonte.render('GAME OVER', True, (255, 0, 0))

                self.tela.blit(texto, (180, 150))


                pygame.display.update()