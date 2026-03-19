from code.Entity import Entity

class Item(Entity):
    def __init__(self, x, y, width, height, sprite=None):
        super().__init__(x, y, width, height, sprite)
        self.collected = False

    def collect(self):
        self.collected = True

    def update(self):
        pass