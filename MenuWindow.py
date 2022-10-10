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
            if event.type == pygame.MOUSEBUTTONDOWN:
                ## if mouse is pressed get position of cursor ##
                pos = pygame.mouse.get_pos()
                if self.test.collidepoint(pos):
                    Game.mode = "test"
                    pygame.draw.rect(self.screen, '#D1A38C', [250, 10, 250, 60], 5)
                    pygame.draw.rect(self.screen, 'darkgreen', [10, 10, 200, 60], 5)
                    #todo zistit ako vyriesit TypeError: initialize_fields() missing 1 required positional argument: 'max_y'
                    Game.load_game(Game,'mapa1.txt')
                    print('test')
                if self.experiment.collidepoint(pos):
                    #todo nema riesenie dat prec oramovanie nech moze vybrat, pridanie zadania a ulozenie
                    Game.mode = "experimental"
                    pygame.draw.rect(self.screen, '#D1A38C', [10, 10, 200, 60], 5)
                    pygame.draw.rect(self.screen, 'darkgreen', [250, 10, 250, 60], 5)
                    Game.has_solution = True
                    Game.max_x = 10
                    Game.max_y = 10
                    Game.initialize_fields(Game, Game.max_x, Game.max_y)
                    Game.fields[(0, 0)].set_has_player(True)
                    Game.player = Player(0, 0)
                    print('experiment')
        pygame.display.update()

    def draw(self):
        ...

