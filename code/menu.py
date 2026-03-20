import pygame

class Menu:
    def __init__(self):
        self.background = pygame.image.load("assets/backgroundMenu.png")
        self.background = pygame.transform.scale(self.background, (800, 600))



    def draw(self, screen):
            # 🎨 fundo
            screen.blit(self.background, (0, 0))

            # 🔤 fontes
            title_font = pygame.font.SysFont("arial", 80, bold=True)
            info_font = pygame.font.SysFont("arial", 28, bold=True)

            screen_width = screen.get_width()

            # 🐱 TÍTULO (com sombra)
            cat = title_font.render("Cat", True, (255, 255, 255))
            cat_shadow = title_font.render("Cat", True, (0, 0, 0))

            adventure = title_font.render("Adventure", True, (255, 255, 255))
            adventure_shadow = title_font.render("Adventure", True, (0, 0, 0))

            cat_x = screen_width // 2 - cat.get_width() // 2
            adv_x = screen_width // 2 - adventure.get_width() // 2

            # sombra
            screen.blit(cat_shadow, (cat_x + 3, 103))
            screen.blit(adventure_shadow, (adv_x + 3, 183))

            # texto
            screen.blit(cat, (cat_x, 100))
            screen.blit(adventure, (adv_x, 180))

            # 🎮 INSTRUÇÃO PRINCIPAL
            start_text = info_font.render("Pressione ENTER para começar", True, (255, 255, 255))
            screen.blit(start_text, (screen_width // 2 - start_text.get_width() // 2, 320))

            # 🎮 CONTROLES
            controls = [
                "Setas: mover",
                "Espaço: pular",
                "E: pegar rato"
            ]

            for i, line in enumerate(controls):
                text = info_font.render(line, True, (0, 0, 0))
                screen.blit(text, (screen_width // 2 - text.get_width() // 2, 420 + i * 35))

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return "start"
        return None