import pygame
import sys
from code.menu import Menu
from code.level import Level


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Cat Adventure")

        self.clock = pygame.time.Clock()
        self.running = True

        self.menu = Menu()
        self.high_score = self.load_high_score()
        self.level = Level(self.high_score)

        self.state = "menu"

        self.menu_bg = pygame.transform.scale(
            pygame.image.load("./assets/backgroundMenu.png"), (800, 600)
        )

        self.game_bg = pygame.transform.scale(
            pygame.image.load("./assets/City2_pale.png"), (800, 600)
        )

        pygame.mixer.music.load("assets/music.wav")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

    def run(self):
        while self.running:
            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.handle_events(event)

            self.update(keys)
            self.draw()

            pygame.display.update()
            self.clock.tick(60)

    def handle_events(self, event):
        if self.state == "menu":
            action = self.menu.handle_input(event)
            if action == "start":
                self.level = Level(self.high_score)
                self.state = "game"

        elif self.state == "game":
            if self.level.game_over:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    if self.level.score > self.high_score:
                        self.high_score = self.level.score
                        self.save_high_score()
                    self.state = "menu"
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.level.player.jump()

    def update(self, keys):
        if self.state == "game":
            self.level.update(keys)

    def draw(self):
        if self.state == "menu":
            self.screen.blit(self.menu_bg, (0, 0))
            self.menu.draw(self.screen, self.high_score)

        elif self.state == "game":
            self.screen.blit(self.game_bg, (0, 0))
            self.level.draw(self.screen)

    def load_high_score(self):
        try:
            with open("highscore.txt", "r") as file:
                return int(file.read())
        except:
            return 0

    def save_high_score(self):
        with open("highscore.txt", "w") as file:
            file.write(str(self.high_score))