import pygame
from code.Entity import Entity

class Player(Entity):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, None)
        self.speed = 5

        # 🔽 GRAVIDADE
        self.velocity_y = 0
        self.gravity = 0.5
        self.jump_force = -10
        self.is_jumping = True

        # 🔽 Sprites para cada direção
        self.sprite_right = pygame.image.load("assets/gato.png")
        self.sprite_left = pygame.transform.flip(self.sprite_right, True, False)  # espelha horizontalmente
        self.sprite_right = pygame.transform.scale(self.sprite_right, (self.width, self.height))
        self.sprite_left = pygame.transform.scale(self.sprite_left, (self.width, self.height))

        self.sprite = self.sprite_right
        self.facing_right = True

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
            self.sprite = self.sprite_left
            self.facing_right = False
        elif keys[pygame.K_RIGHT]:
            self.x += self.speed
            self.sprite = self.sprite_right
            self.facing_right = True

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
        screen.blit(self.sprite, (self.x, self.y))