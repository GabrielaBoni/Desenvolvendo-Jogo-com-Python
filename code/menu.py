import pygame


class Menu:
    def __init__(self):
        self.background = pygame.transform.scale(
            pygame.image.load("assets/backgroundMenu.png"), (800, 600)
        )

    def draw(self, screen, high_score):
        screen.blit(self.background, (0, 0))

        title_font = pygame.font.SysFont("arial", 80, bold=True)
        info_font = pygame.font.SysFont("arial", 28, bold=True)
        score_font = pygame.font.SysFont("arial", 32, bold=True)

        screen_width = screen.get_width()

        cat = title_font.render("Cat", True, (255, 255, 255))
        cat_shadow = title_font.render("Cat", True, (0, 0, 0))

        adventure = title_font.render("Adventure", True, (255, 255, 255))
        adventure_shadow = title_font.render("Adventure", True, (0, 0, 0))

        cat_x = screen_width // 2 - cat.get_width() // 2
        adv_x = screen_width // 2 - adventure.get_width() // 2

        screen.blit(cat_shadow, (cat_x + 3, 103))
        screen.blit(adventure_shadow, (adv_x + 3, 183))

        screen.blit(cat, (cat_x, 100))
        screen.blit(adventure, (adv_x, 180))

        start_text = info_font.render("Pressione ENTER para começar", True, (255, 255, 255))
        screen.blit(start_text, (screen_width // 2 - start_text.get_width() // 2, 320))

        controls = [
            "Setas: mover",
            "Espaço: pular"
        ]

        for i, line in enumerate(controls):
            text = info_font.render(line, True, (0, 0, 0))
            screen.blit(text, (screen_width // 2 - text.get_width() // 2, 420 + i * 35))

        score_text = score_font.render(f"Recorde: {high_score}", True, (0, 0, 0))
        screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, 520))

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            return "start"
        return None