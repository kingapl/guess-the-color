import pygame


class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Guess the color")

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((197, 202, 207))

            pygame.display.flip()

        pygame.quit()


if __name__ == '__main__':
    app = App()
    app.run()
