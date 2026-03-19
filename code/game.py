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

        self.background = pygame.image.load("./assets/backgroundMenu.png")
        self.background = pygame.transform.scale(self.background, (800, 600))

    def run(self):
        pygame.mixer.music.load("assets/music.wav")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

        while self.running:
            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if self.state == "menu":
                    action = self.menu.handle_input(event)
                    if action == "start":
                        self.state = "game"

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.level.player.jump()

            self.screen.blit(self.background, (0, 0))

            if self.state == "menu":
                self.menu.draw(self.screen)
            else:
                self.level.update(keys)
                self.level.draw(self.screen)

            pygame.display.update()
            self.clock.tick(60)
