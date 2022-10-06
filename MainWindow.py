import pygame

from Game import Game
from MenuWindow import MenuWindow


class MainWindow:
    window_width = 600
    window_height = 600
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Slimak - Minisoft 1")

        self.screen = pygame.display.set_mode((MainWindow.window_width, MainWindow.window_height))
        rect_game = pygame.Rect(150, 150, Game.window_width, Game.window_height)
        rect_menu = pygame.Rect(0, 0, MenuWindow.window_width, MenuWindow.window_height)

        self.screen.fill('#E8CAB0')

        self.font = pygame.font.SysFont('Arial', 25)

        pygame.draw.rect(self.screen, 'white', pygame.Rect(10, 200, 130, 200))
        self.screen.blit(self.font.render('Zadanie:', True, (0,50,0)), (10, 200))
        self.screen.blit(self.font.render('Nema riesenie', True, (0, 50, 0)), (10, 410))
        pygame.draw.rect(self.screen, 'darkgreen', [5, 410, 140, 60], 5)

        game_screen = self.screen.subsurface(rect_game)
        filepath = "mapa1.txt"
        self.game = Game(filepath, game_screen)

        menu_screen = self.screen.subsurface(rect_menu)
        self.menu = MenuWindow(menu_screen)
        # self.menu.main_loop()


        self.game.main_loop()
        self.clock = pygame.time.Clock()
        self.screen.fill((0, 0, 0))