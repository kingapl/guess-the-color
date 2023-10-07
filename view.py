from abc import ABC, abstractmethod

from settings import Settings


class View(ABC):
    def __init__(self, game, background_color):
        self.game = game
        self.settings = Settings()
        self.game.screen.fill(background_color)

    @abstractmethod
    def display(self):
        pass
