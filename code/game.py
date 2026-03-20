import pygame

from code.player import Player

class Game:
    def __init__(self):
        # tamanho da tela
        self.largura = 600
        self.altura = 400

        # criar janela
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption('Desvie dos objetos')

        # controle de tempo
        self.clock = pygame.time.Clock()

        # controle de jogo
        self.rodando = True

        # classe player
        self.player = Player(250, 350)

    def run(self):
        while self.rodando:
            self.clock.tick(60)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.rodando = False

            # classe player
            teclas = pygame.key.get_pressed()
            self.player.mover(teclas)

            self.tela.fill((0, 0, 0))

            self.player.desenhar(self.tela)

            pygame.display.update()