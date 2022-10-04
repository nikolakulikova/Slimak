import sys

import pygame


class MenuWindow:
    window_width = 600
    window_height = 150

    def __init__(self, screen):
        self.screen = screen
        self.screen.fill('#D1A38C')
        imp = pygame.image.load("tlacitko_test.png").convert()
        imp = pygame.transform.scale(imp, (200, 60))
        screen.blit(imp, (10, 10))

        imp = pygame.image.load("tlacitko_expetiment.png").convert()
        imp = pygame.transform.scale(imp, (250, 60))
        screen.blit(imp, (250, 10))

        pygame.draw.rect(self.screen, 'darkgreen', [250, 10, 250, 60], 5)
        # pygame.draw.rect(self.screen, 'white', pygame.Rect(10, 200, 130, 200))

    def main_loop(self):
        while True:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

    def draw(self):
        ...

