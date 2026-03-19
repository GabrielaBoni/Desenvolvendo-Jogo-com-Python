from code.player import Player
from code.enemy import Enemy
from code.Item import Item
from code.platform_game import Platform

class Level:
    def __init__(self):
        self.player = Player(100, 300, 50, 50)
        self.enemies = [Enemy(500, 300, 50, 50)]
        self.items = [Item(300, 250, 30, 30)]
        self.platforms = [Platform(0, 350, 800, 50)]

    def update(self, keys):
        self.player.update(keys)

        for enemy in self.enemies:
            enemy.update()

    def draw(self, screen):
        self.player.draw(screen)

        for enemy in self.enemies:
            enemy.draw(screen)

        for item in self.items:
            if not item.collected:
                item.draw(screen)

        for platform in self.platforms:
            platform.draw(screen)