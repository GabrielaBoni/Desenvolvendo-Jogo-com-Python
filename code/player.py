import pygame

from code.Entity import Entity

class Player(Entity):
    def __init__(self, x, y, width, height, sprite=None):
        super().__init__(x, y, width, height, sprite)

        self.speed = 5

        # 🔽 GRAVIDADE
        self.velocity_y = 0
        self.gravity = 0.5
        self.jump_force = -10

        self.is_jumping = True  # começa caindo

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

    def jump(self):
        if not self.is_jumping:
            self.velocity_y = self.jump_force
            self.is_jumping = True

    def apply_gravity(self):
        self.velocity_y += self.gravity
        self.y += self.velocity_y

    def update(self, keys):
        self.move(keys)
        self.apply_gravity()

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.width, self.height))