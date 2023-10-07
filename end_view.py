import pygame

from text import Text
from view import View


class EndView(View):
    SCORE = "Twój wynik to %s punktów"
    AVERAGE = "Średni czas Twoich odpowiedzi to %s sekund"
    START_INFO = "Aby rozpocząć od nowa naciśnij ENTER"

    def __init__(self, game, points, average, background_color):
        super().__init__(game, background_color)
        self.score = Text(self.game.screen, EndView.SCORE % points, self.settings.black, None, 40)
        self.average = Text(self.game.screen, EndView.AVERAGE % round(average, 4), self.settings.black, None, 40)
        self.info = Text(self.game.screen, EndView.START_INFO, self.settings.black, None, 26)

    def display(self):
        self.score.display(self.game.screen_rect.centerx - (self.score.width / 2), 300)
        self.average.display(self.game.screen_rect.centerx - (self.average.width / 2), 350)
        self.info.display(self.game.screen_rect.centerx - (self.info.width / 2), 430)
        self.game.screen.blit(self.game.screen, (0, 0))
        pygame.display.flip()
