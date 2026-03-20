import pygame
from code.Entity import Entity

class Enemy(Entity):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, None)
        self.speed = 2
        self.direction = 1  # 1 = direita | -1 = esquerda

        # limites de patrulha
        self.min_x = x - 500
        self.max_x = x + 300

        # 🔽 Sprites para cada direção
        self.sprite_right = pygame.image.load("assets/cachorro.png")
        self.sprite_left = pygame.transform.flip(self.sprite_right, True, False)
        self.sprite_right = pygame.transform.scale(self.sprite_right, (self.width, self.height))
        self.sprite_left = pygame.transform.scale(self.sprite_left, (self.width, self.height))

        self.sprite = self.sprite_right

    def update(self):
        self.x += self.speed * self.direction

        # troca direção ao atingir limite
        if self.x <= self.min_x or self.x + self.width >= self.max_x:
            self.direction *= -1

        # atualiza sprite conforme direção
        if self.direction > 0:
            self.sprite = self.sprite_right
        else:
            self.sprite = self.sprite_left

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))