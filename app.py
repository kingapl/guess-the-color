from random import choice

import pygame


class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Guess the color")

        self.font = pygame.font.Font(pygame.font.get_default_font(), 100)
        self.colors = {
            "brązowy": (79, 33, 13),
            "czarny": (0, 0, 0),
            "czerwony": (217, 7, 7),
            "fioletowy": (102, 11, 133),
            "niebieski": (12, 12, 196),
            "pomarańczowy": (227, 81, 14),
            "różowy": (237, 17, 164),
            "szary": (74, 72, 73),
            "zielony": (28, 158, 19),
            "żółty": (253, 219, 4),
        }

    def run(self):
        running = True
        chosen = False

        color_name = None
        color = None

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((197, 202, 207))

            if not chosen:
                color_name = choice(list(self.colors.keys()))
                color = choice(list(self.colors.values()))

                while color == self.colors[color_name]:
                    color = choice(list(self.colors.values()))
                chosen = True

            text_surface = self.font.render(color_name, True, color)
            text_width = text_surface.get_rect().width

            self.screen.blit(text_surface, (self.screen_rect.centerx - (text_width / 2), 100))

            pygame.display.flip()

        pygame.quit()


if __name__ == '__main__':
    app = App()
    app.run()
