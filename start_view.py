import pygame

from text import Text
from view import View


class StartView(View):
    TARGET_INFO = "Odpowiedz poprawnie jakiego koloru są litery"
    INSTRUCTION = "Wskazuj odpowiedzi naciskając strzałkę w lewo lub w prawo"
    START_INFO = "Aby rozpocząć naciśnij ENTER"

    def __init__(self, game, background_color):
        super().__init__(game, background_color)
        self.target = Text(self.game.screen, StartView.TARGET_INFO, self.settings.black, None, 40)
        self.instruction = Text(self.game.screen, StartView.INSTRUCTION, self.settings.black, None, 40)
        self.info = Text(self.game.screen, StartView.START_INFO, self.settings.black, None, 26)

    def display(self):
        self.target.display(self.game.screen_rect.centerx - (self.target.width / 2), 300)
        self.instruction.display(self.game.screen_rect.centerx - (self.instruction.width / 2), 350)
        self.info.display(self.game.screen_rect.centerx - (self.info.width / 2), 430)
        self.game.screen.blit(self.game.screen, (0, 0))
        pygame.display.flip()
