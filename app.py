from datetime import datetime
from random import choice

import pygame

from arrow import Arrow
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
        self.end = False
        self.guessing_attempts = 10
        self.points = 0
        self.chosen = False
        self.color_to_guess = None
        self.answer1 = None
        self.answer2 = None
        self.left_arrow = Arrow(self.screen, "images/left-arrow.png")
        self.right_arrow = Arrow(self.screen, "images/right-arrow.png")
        self.points_text = None
        self.start_time = None
        self.end_time = None
        self.durations = []

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

        while self.running:
            self._check_events()
            if not self.end:
                if not self.chosen:
                    color, color_name = self._choose_color(self.colors)

                    self.color_to_guess = Text(self.screen, color_name, color, self._get_color_name_from_rbg(color),
                                               self.settings.color_font_size)

                    answers = {self._get_color_name_from_rbg(color), color_name}

                    self.answer1 = Text(self.screen, answers.pop(), self.settings.black, None,
                                        self.settings.answer_font_size)
                    self.answer2 = Text(self.screen, answers.pop(), self.settings.black, None,
                                        self.settings.answer_font_size)

                    self.chosen = True
                    self.start_time = datetime.now()

                self._update_points()
                self._update_screen()

        pygame.quit()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self._check_answer(self.answer1):
                        self.points += 1
                    self.end_time = datetime.now()
                    self.chosen = False
                    self.guessing_attempts -= 1
                    self.durations.append((self.end_time - self.start_time).total_seconds())
                if event.key == pygame.K_RIGHT:
                    if self._check_answer(self.answer2):
                        self.points += 1
                    self.end_time = datetime.now()
                    self.chosen = False
                    self.guessing_attempts -= 1
                    self.durations.append((self.end_time - self.start_time).total_seconds())

    def _check_answer(self, answer):
        return answer.text == self.color_to_guess.letters_color_name

    def _get_color_name_from_rbg(self, color):
        return list(self.colors.keys())[list(self.colors.values()).index(color)]

    def _choose_color(self, colors):
        color_name = choice(list(colors.keys()))
        color = choice(list(colors.values()))

        while color == colors[color_name]:
            color = choice(list(colors.values()))

        return color, color_name

    def _update_points(self):
        self.points_text = Text(self.screen, str(self.points), self.settings.black, None, 40)

    def _calculate_average(self):
        return sum(self.durations) / len(self.durations)

    def _update_screen(self):
        self.screen.fill(self.settings.background_color)

        self.points_text.display(self.settings.screen_width - 70, 50)

        self.color_to_guess.display(self.screen_rect.centerx - (self.color_to_guess.width / 2), 100)
        self.left_arrow.display(30, self.settings.screen_height - self.left_arrow.rect.height)
        self.right_arrow.display(self.settings.screen_width - self.right_arrow.rect.width - 30,
                                 self.settings.screen_height - self.right_arrow.rect.height)
        self.answer1.display(160, 500)
        self.answer2.display(self.settings.screen_width - self.answer2.width - 160, 500)

        if self.guessing_attempts == 0:
            score = Text(self.screen, f'Twój wynik to {self.points} punktów', self.settings.black, None, 40)
            score.display(self.screen_rect.centerx - (score.width / 2), 300)

            average = Text(self.screen,
                           f"Średni czas Twoich odpowiedzi to {str(round(self._calculate_average(), 4))} sekund",
                           self.settings.black, None, 40)
            average.display(self.screen_rect.centerx - (average.width / 2), 350)

            self.end = True

        pygame.display.flip()


if __name__ == '__main__':
    app = App()
    app.run()
