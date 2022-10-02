import sys

import pygame


class MenuWindow:
    window_width = 600
    window_height = 200

    def __init__(self, screen):
        self.screen = screen
        self.screen.fill((0, 0, 255))

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

