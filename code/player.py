import pygame

from code.Entity import Entity

class Player(Entity):
    def __init__(self, x, y, width, height, sprite=None):
        super().__init__(x, y, width, height, sprite)
        self.speed = 5
        self.velocity_y = 0
        self.is_jumping = False

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

    def jump(self):
        if not self.is_jumping:
            self.velocity_y = -10
            self.is_jumping = True

    def apply_gravity(self):
        gravity = 0.5
        self.velocity_y += gravity
        self.y += self.velocity_y

    def update(self,keys):
        self.move(keys)
        self.apply_gravity()