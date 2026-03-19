from code.Entity import Entity

class Enemy(Entity):
    def __init__(self, x, y, width, height, sprite=None):
        super().__init__(x, y, width, height, sprite)
        self.speed = 2

    def move(self):
        self.x -= self.speed  # exemplo simples

    def update(self):
        self.move()