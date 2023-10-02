import pygame


class Arrow:
    def __init__(self, screen, img):
        self.screen = screen
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (576, 288))
        self.rect = self.image.get_rect()

    def display(self, x, y):
        self.screen.blit(self.image, (x, y))
