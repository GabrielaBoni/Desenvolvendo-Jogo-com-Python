import pygame
import random

from code.player import Player
from code.enemy import Enemy
from code.Item import Item
from code.platform_game import Platform

class Level:
    def __init__(self):
        self.ground_y = 550  # altura do chão
        self.platforms = [Platform(0, self.ground_y, 800, 50)]
        self.player = Player(100, self.ground_y - 50, 50, 50)
        self.enemies = [Enemy(500, self.ground_y - 50, 50, 50)]

        self.items = []  # 👈 IMPORTANTE
        self.spawn_item()  # 👈 cria o primeiro rato

        self.lives = 4
        self.game_over = False

        self.score = 0

    def update(self, keys):
        if self.game_over:
            return  # para tudo

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
                # 👇 encostou na plataforma
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
                print("Você foi atingido!")

                self.lives -= 1
                print(f"Vidas restantes: {self.lives}")

                # 🔁 reset do player
                self.player.x = 100
                self.player.y = 100
                self.player.velocity_y = 0

                if self.lives <= 0:
                    self.game_over = True

    def draw(self, screen):
        self.player.draw(screen)

        for enemy in self.enemies:
            enemy.draw(screen)

        for item in self.items:
            if not item.collected:
                item.draw(screen)

        for platform in self.platforms:
            platform.draw(screen)

        if self.game_over:
            font = pygame.font.SysFont("arial", 60, bold=True)
            text = font.render("GAME OVER", True, (255, 0, 0))
            screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, 250))

        font = pygame.font.SysFont("arial", 30)
        lives_text = font.render(f"Vidas: {self.lives}", True, (0, 0, 0))
        screen.blit(lives_text, (10, 10))

        font = pygame.font.SysFont("arial", 30)

        score_text = font.render(f"Pontos: {self.score}", True, (0, 0, 0))
        screen.blit(score_text, (650, 10))

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

                    item.collected = True

                    self.score += 1
                    print(f"Pontos: {self.score}")

                    # 🐭 cria outro rato
                    self.spawn_item()

    def spawn_item(self):
        x = random.randint(50, 750)

        # 🐭 altura controlada (alcançável)
        y = random.randint(self.ground_y - 150, self.ground_y - 40)

        self.items = [Item(x, y, 30, 30)]