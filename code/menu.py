import pygame

class Menu:
    def __init__(self):
        self.selected_option = 0
        self.options = ["Iniciar", "Sair"]

    def draw(self, screen):
        font = pygame.font.SysFont(None, 40)

        for i, option in enumerate(self.options):
            text = font.render(option, True, (255, 255, 255))
            screen.blit(text, (100, 100 + i * 50))

        instructions = font.render("Setas: mover | Espaço: pular", True, (200, 200, 200))
        screen.blit(instructions, (100, 300))

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return "start"
        return None