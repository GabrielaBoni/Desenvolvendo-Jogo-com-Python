import pygame
import random

from code.player import Player
from code.enemy import Enemy
from code.Item import Item
from code.platform_game import Platform


class Level:
    def __init__(self, high_score=0):

        self.ground_y = 550
        self.platforms = [Platform(0, self.ground_y, 800, 50)]

        self.player = Player(100, self.ground_y - 50, 50, 50)

        self.enemies = [Enemy(500, self.ground_y - 50, 50, 50)]

        self.items = []
        self.spawn_item()

        self.lives = 4
        self.score = 0
        self.high_score = high_score
        self.game_over = False

        self.sound_pick = pygame.mixer.Sound("assets/pegarRato.mp3")
        self.sound_hit = pygame.mixer.Sound("assets/pegarGato.mp3")
        self.sound_gameover = pygame.mixer.Sound("assets/GameOver.mp3")


    def update(self, keys):
        if self.game_over:
            return

        self.player.update(keys)

        self.check_collisions()
        self.check_item_collection()
        self.check_enemy_collision()

        for enemy in self.enemies:
            enemy.update()


    def check_collisions(self):
        for platform in self.platforms:
            if (
                self.player.x < platform.x + platform.width and
                self.player.x + self.player.width > platform.x and
                self.player.y + self.player.height <= platform.y + 10 and
                self.player.y + self.player.height + self.player.velocity_y >= platform.y
            ):
                self.player.y = platform.y - self.player.height
                self.player.velocity_y = 0
                self.player.is_jumping = False


    def check_enemy_collision(self):
        for enemy in self.enemies:
            if (
                self.player.x < enemy.x + enemy.width and
                self.player.x + self.player.width > enemy.x and
                self.player.y < enemy.y + enemy.height and
                self.player.y + self.player.height > enemy.y
            ):
                if not self.player.invulnerable:
                    print("Você foi atingido!")

                    self.lives -= 1
                    self.sound_hit.play()

                    self.player.x = 100
                    self.player.y = self.ground_y - self.player.height
                    self.player.velocity_y = 0
                    self.player.is_jumping = False

                    self.player.invulnerable = True
                    self.player.invulnerable_time = 180

                    if self.lives <= 0:
                        self.game_over = True
                        self.sound_gameover.play()


    def check_item_collection(self):
        for item in self.items:
            if not item.collected:
                if (
                    self.player.x < item.x + item.width and
                    self.player.x + self.player.width > item.x and
                    self.player.y < item.y + item.height and
                    self.player.y + self.player.height > item.y
                ):
                    print("Pegou o rato!")

                    self.sound_pick.play()

                    item.collected = True

                    self.score += 1
                    print(f"Pontos: {self.score}")

                    self.spawn_item()

                    if self.score % 5 == 0:
                        for enemy in self.enemies:
                            enemy.speed += 0.5

                    break


    def spawn_item(self):
        x = random.randint(50, 750)
        y = random.randint(self.ground_y - 150, self.ground_y - 40)

        self.items = [Item(x, y, 30, 30)]


    def draw(self, screen):
        self.player.draw(screen)

        for enemy in self.enemies:
            enemy.draw(screen)

        for item in self.items:
            if not item.collected:
                item.draw(screen)

        for platform in self.platforms:
            platform.draw(screen)

        font = pygame.font.SysFont("arial", 30)

        score_text = font.render(f"Pontos: {self.score}", True, (0, 0, 0))
        high_text = font.render(f"Recorde: {self.high_score}", True, (0, 0, 0))
        lives_text = font.render(f"Vidas: {self.lives}", True, (0, 0, 0))

        screen.blit(score_text, (650, 10))
        screen.blit(high_text, (10, 40))
        screen.blit(lives_text, (10, 10))

        if self.game_over:
            font_big = pygame.font.SysFont("arial", 70, bold=True)
            font_small = pygame.font.SysFont("arial", 40, bold=True)

            game_over_text = font_big.render("GAME OVER", True, (255, 0, 0))
            restart_text = font_small.render("PRESSIONE ENTER PARA REINICIAR", True, (0, 0, 0))

            screen_width = screen.get_width()

            screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, 200))
            screen.blit(restart_text, (screen_width // 2 - restart_text.get_width() // 2, 300))