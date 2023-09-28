from random import choice

import pygame

from text import Text
from settings import Settings


class App:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Guess the color")

        self.running = False
        self.color_to_guess = None

        self.colors = {
            "brązowy": self.settings.brown,
            "czarny": self.settings.black,
            "czerwony": self.settings.red,
            "fioletowy": self.settings.purple,
            "niebieski": self.settings.blue,
            "pomarańczowy": self.settings.orange,
            "różowy": self.settings.pink,
            "szary": self.settings.gray,
            "zielony": self.settings.green,
            "żółty": self.settings.yellow,
        }

    def run(self):
        self.running = True
        chosen = False

        while self.running:
            self._check_events()

            if not chosen:
                self._choose_color(self.colors)
                chosen = True

            self._update_screen()

        pygame.quit()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def _choose_color(self, colors):
        color_name = choice(list(colors.keys()))
        color = choice(list(colors.values()))

        while color == colors[color_name]:
            color = choice(list(colors.values()))

        self.color_to_guess = Text(self.screen, color_name, color)

    def _update_screen(self):
        self.screen.fill(self.settings.background_color)

        self.color_to_guess.display(self.screen_rect.centerx - (self.color_to_guess.width / 2), 100)

        pygame.display.flip()


if __name__ == '__main__':
    app = App()
    app.run()
