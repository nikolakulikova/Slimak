import pygame

from Game import Game
from MenuWindow import MenuWindow


class MainWindow:
    window_width = 600
    window_height = 600
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((MainWindow.window_width, MainWindow.window_height))
        rect_game = pygame.Rect(200, 200, Game.window_width, Game.window_height)
        rect_menu = pygame.Rect(0, 0, MenuWindow.window_width, MenuWindow.window_height)

        game_screen = self.screen.subsurface(rect_game)
        filepath = "mapa1.txt"
        self.game = Game(filepath, game_screen)

        menu_screen = self.screen.subsurface(rect_menu)
        self.menu = MenuWindow(menu_screen)
        # self.menu.main_loop()


        self.game.main_loop()
        self.clock = pygame.time.Clock()
        self.screen.fill((0, 0, 0))