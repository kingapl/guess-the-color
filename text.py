import pygame


class Text:
    def __init__(self, screen, text, color, letters_color_name, font_size):
        self.screen = screen
        self.font = pygame.font.Font(pygame.font.get_default_font(), font_size)
        self.surface = self.font.render(text, True, color)
        self.width = self.surface.get_rect().width
        self.text = text
        self.letters_color_name = letters_color_name

    def display(self, x, y):
        self.screen.blit(self.surface, (x, y))
