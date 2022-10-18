import sys

import pygame

from Game import *


class MenuWindow:
    window_width = 600
    window_height = 150

    def __init__(self, screen):
        self.screen = screen
        self.screen.fill('#D1A38C')
        imp = pygame.image.load("tlacitko_test.png").convert()
        imp = pygame.transform.scale(imp, (200, 60))
        self.test = screen.blit(imp, (10, 10))

        imp = pygame.image.load("tlacitko_expetiment.png").convert()
        imp = pygame.transform.scale(imp, (250, 60))
        self.experiment = screen.blit(imp, (250, 10))

        pygame.draw.rect(self.screen, 'darkgreen', [10, 10, 200, 60], 5)                        
        # pygame.draw.rect(self.screen, 'white', pygame.Rect(10, 200, 130, 200))

    def main_loop(self):
        self.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        buttons = pygame.mouse.get_pressed()

        if any(buttons):  # for any mouse button
            pos = pygame.mouse.get_pos()
            if self.experiment.collidepoint(pos):
                # todo nema riesenie dat prec oramovanie nech moze vybrat, pridanie zadania a ulozenie
                Game.mode = "experimental"
                pygame.draw.rect(self.screen, '#D1A38C', [10, 10, 200, 60], 5)
                pygame.draw.rect(self.screen, 'darkgreen', [250, 10, 250, 60], 5)
                Game.has_solution = True
                Game.max_x = 6
                Game.max_y = 6
                Game.initialize_fields(Game.max_x, Game.max_y)
                Game.fields[(0, 0)].set_has_player(True)
                Game.player = Player(0, 0)
                pygame.display.update()
            if self.test.collidepoint(pos):
                Game.mode = "test"
                pygame.draw.rect(self.screen, '#D1A38C', [250, 10, 250, 60], 5)
                pygame.draw.rect(self.screen, 'darkgreen', [10, 10, 200, 60], 5)
                Game.load_game('mapa1.txt')
                pygame.display.update()

    def draw(self):
        ...

