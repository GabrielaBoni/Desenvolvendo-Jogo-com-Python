import pygame

class Entity:
    def __init__(self, x, y, width, height, sprite=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sprite = sprite

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        pass

    def draw(self, screen):
        if self.sprite:
            screen.blit(self.sprite, (self.x, self.y))
        else:
            pygame.draw.rect(screen, (255, 0, 0), self.get_rect())