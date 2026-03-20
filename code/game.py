import pygame
import sys
from code.menu import Menu
from code.level import Level


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Cat Adventure")

        self.clock = pygame.time.Clock()
        self.running = True

        self.menu = Menu()
        self.level = Level()

        self.state = "menu"

        # 🎨 BACKGROUND MENU
        self.menu_bg = pygame.image.load("./assets/backgroundMenu.png")
        self.menu_bg = pygame.transform.scale(self.menu_bg, (800, 600))

        # 🎨 BACKGROUND JOGO
        self.game_bg = pygame.image.load("./assets/City2_pale.png")
        self.game_bg = pygame.transform.scale(self.game_bg, (800, 600))

    def run(self):
        # 🎵 Música
        pygame.mixer.music.load("assets/music.wav")  # 👉 TROQUE se quiser outro nome
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

        while self.running:
            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # 🎮 INPUT DO MENU
                if self.state == "menu":
                    action = self.menu.handle_input(event)
                    if action == "start":
                        self.state = "game"

                # 🎮 INPUT DO JOGO
                if self.state == "game":
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.level.player.jump()

            # 🎨 BACKGROUND (muda conforme estado)
            if self.state == "menu":
                self.screen.blit(self.menu_bg, (0, 0))
                # 👉 COLOQUE A IMAGEM DO MENU AQUI
            else:
                self.screen.blit(self.game_bg, (0, 0))
                # 👉 COLOQUE A IMAGEM DO JOGO AQUI

            # 🎮 DESENHO
            if self.state == "menu":
                self.menu.draw(self.screen)
            else:
                self.level.update(keys)
                self.level.draw(self.screen)

            pygame.display.update()
            self.clock.tick(60)
