import pygame
from code.Entity import Entity

class Item(Entity):
    def __init__(self, x, y, width, height, sprite=None):
        super().__init__(x, y, width, height, sprite)
        self.collected = False

        self.sprite = pygame.image.load("assets/rato.png")
        self.sprite = pygame.transform.scale(self.sprite, (self.width + 20, self.height))

    def collect(self):
        self.collected = True

    def update(self):
        pass

    def draw(self, screen):
        if not self.collected:
            screen.blit(self.sprite, (self.x, self.y))