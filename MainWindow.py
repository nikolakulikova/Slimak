import pygame
import tkinter as tk
from tkinter import ttk
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

        self.solution_button = self.screen.blit(self.font.render('Nema riesenie', True, (0, 50, 0)), (10, 410))

        self.has_solution = True

        game_screen = self.screen.subsurface(rect_game)
        filepath = "mapa1.txt"
        self.game = Game(filepath, game_screen)

        menu_screen = self.screen.subsurface(rect_menu)
        self.menu = MenuWindow(menu_screen)
        # self.menu.main_loop()


        # self.game.main_loop()
        self.main_loop()
        self.clock = pygame.time.Clock()
        self.screen.fill((0, 0, 0))

    def main_loop(self):
        while True:

            self.menu.main_loop()
            self.game.main_loop()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    ## if mouse is pressed get position of cursor ##
                    pos = pygame.mouse.get_pos()
                    if 5 < pos[0] < 180 and 410 < pos[1] < 430:
                        if Game.mode == 'experimental':
                            self.has_solution = not self.has_solution
                            if self.has_solution:
                                pygame.draw.rect(self.screen, 'darkgreen', [5, 410, 140, 60], 5)
                            else:
                                pygame.draw.rect(self.screen, '#E8CAB0', [5, 410, 140, 60], 5)
                        else:
                            ...
                            # toDo nejaka info ci dobre oznacil, mne nejde dat pop up window mac hadze chybu

                            print('aaa')
                    if self.save_button:
                        if self.save_button.collidepoint(pos):
                            Game.save_as_file('solution.txt', self.has_solution)
            pygame.display.update()




