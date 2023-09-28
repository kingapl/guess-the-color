import pygame

from settings import Settings


class Text:
    def __init__(self, screen, text, color):
        self.settings = Settings()
        self.screen = screen
        self.font = pygame.font.Font(pygame.font.get_default_font(), self.settings.font_size)
        self.surface = self.font.render(text, True, color)
        self.width = self.surface.get_rect().width

    def display(self, x, y):
        self.screen.blit(self.surface, (x, y))
