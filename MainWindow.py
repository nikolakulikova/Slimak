import time

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
        self.screen.blit(self.font.render('Prejdi slimákom cez', True, (0, 50, 0)), (10, 200))
        self.screen.blit(self.font.render('všetky políčka a', True, (0, 50, 0)), (10, 250))
        self.screen.blit(self.font.render('vyhni sa prekážkam.', True, (0, 50, 0)), (10, 300))

        self.solution_button = self.screen.blit(self.font.render('Nema riesenie', True, (0, 50, 0)), (10, 410))

        self.has_solution = True

        game_screen = self.screen.subsurface(rect_game)
        filepath = "mapa9.txt"
        Game.initialize(filepath, game_screen)
        if Game.mode == 'experimental':
            self.save_button = self.screen.blit(self.font.render('Ulozit', True, (0, 50, 0)), (10, 200))
        else:
            self.save_button = None

        menu_screen = self.screen.subsurface(rect_menu)
        self.menu = MenuWindow(menu_screen)
        self.main_loop()
        self.clock = pygame.time.Clock()
        self.screen.fill((0, 0, 0))

    def main_loop(self):
        while True:
            self.menu.main_loop()
            Game.main_loop()
            buttons = pygame.mouse.get_pressed()

            if any(buttons):  # for any mouse button
                pos = pygame.mouse.get_pos()
                if self.solution_button.collidepoint(pos):
                    if Game.mode == 'experimental':
                        self.has_solution = not self.has_solution
                        if not self.has_solution:
                            pygame.draw.rect(self.screen, 'darkgreen', [5, 410, 140, 60], 5)
                        else:
                            pygame.draw.rect(self.screen, '#E8CAB0', [5, 410, 140, 60], 5)
                        pygame.display.update()
                        time.sleep(0.5)
                    else:
                        ...
                        # toDo nejaka info ci dobre oznacil, mne nejde dat pop up window mac hadze chybu

                if self.save_button:
                    if self.save_button.collidepoint(pos):
                        Game.save_as_file('solution.txt', self.has_solution)
                        pygame.display.update()


