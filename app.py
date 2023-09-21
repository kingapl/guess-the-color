import pygame


class App:
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Guess the color")

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((197, 202, 207))

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    app = App()
