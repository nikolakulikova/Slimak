import time
from turtle import color, window_height, window_width

import pygame
import tkinter as tk
from tkinter import Menu, ttk
from Game import Game
from MenuWindow import MenuWindow


class MainWindow:
    window_width = 600
    window_height = 600
    solved_level = [False] * 10

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Slimak - Minisoft 1")

        self.screen = pygame.display.set_mode((MainWindow.window_width, MainWindow.window_height))
        self.rect_game = pygame.Rect(150, 150, Game.window_width, Game.window_height)
        self.rect_menu = pygame.Rect(0, 0, MenuWindow.window_width, MenuWindow.window_height)

        self.screen.fill('#E8CAB0')

        self.font = pygame.font.SysFont('Arial', 20)
        self.screen.blit(self.font.render('Prejdi slimákom', True, (0, 50, 0)), (10, 200))
        self.screen.blit(self.font.render('cez všetky políčka', True, (0, 50, 0)), (10, 250))
        self.screen.blit(self.font.render('a vyhni sa', True, (0, 50, 0)), (10, 300))
        self.screen.blit(self.font.render('prekážkam.', True, (0, 50, 0)), (10, 350))

        imp = pygame.image.load("neni_riesenia.png").convert()
        imp = pygame.transform.scale(imp, (150, 45))
        self.solution_button = self.screen.blit(imp, (0, 410))

        self.level_number = 1
        self.has_solution = True

        game_screen = self.screen.subsurface(self.rect_game)
        filepath = "mapa" + str(self.level_number) + ".txt"
        Game.initialize(filepath, game_screen)
        if Game.mode == 'experimental':
            self.save_button = self.screen.blit(self.font.render('Ulozit', True, (0, 50, 0)), (10, 200))
        else:
            self.save_button = None
            imp = pygame.image.load("restart.png").convert()
            imp = pygame.transform.scale(imp, (70, 70))
            self.restart_button = self.screen.blit(imp, (5, 480))

            imp = pygame.image.load("sipka.png").convert()
            imp = pygame.transform.scale(imp, (70, 70))
            self.next_button = self.screen.blit(imp, (75, 480))

        menu_screen = self.screen.subsurface(self.rect_menu)
        self.menu = MenuWindow(menu_screen)
        self.font = pygame.font.SysFont('Arial', 30)
        self.level_and_score = self.screen.blit(self.font.render('level 1   skóre:0/10', True, (0, 50, 0)), (30, 80))
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
                        if Game.has_solution:
                            imp = pygame.image.load("nespravne.png").convert()
                            imp = pygame.transform.scale(imp, (150, 45))
                            self.solution_button = self.screen.blit(imp, (0, 410))

                        else:
                            imp = pygame.image.load("spravne.png").convert()
                            imp = pygame.transform.scale(imp, (150, 45))
                            self.solution_button = self.screen.blit(imp, (0, 410))

                            self.solved_level[self.level_number-1] = True

                            self.update_level_and_score()
                        
                if not Game.mode == 'experimental' and self.restart_button.collidepoint(pos):
                    self.load_game()

                if not Game.mode == 'experimental' and self.next_button.collidepoint(pos):
                    self.level_number += 1
                    if self.level_number > 10:
                        self.level_number -= 1
                        score = 0
                        for lvl in self.solved_level:
                            if lvl:
                                score+=1
                        self.screen.fill(pygame.Color("#D1A38C"), (30, 80, self.window_width, 40))
                        self.level_and_score = self.screen.blit(self.font.render('Hurá! Prešiel si všetky levely. Tvoje skóre je: ' +str(score)+'/10', True, (0, 50, 0)), (30, 80))
                        continue

                    self.update_level_and_score()
                    self.load_game()


                if Game.mode == 'experimental':
                    self.save_button = self.screen.blit(self.font.render('Ulozit', True, (0, 50, 0)), (10, 200))
                else:
                    self.save_button = None

                if self.save_button:
                    if self.save_button.collidepoint(pos):
                        Game.save_as_file('solution.txt', self.has_solution)
                        pygame.display.update()

            if not self.solved_level[self.level_number-1] and Game.total_number_of_free_fields == len(Game.player.path):
                self.solved_level[self.level_number-1] = True
                imp = pygame.image.load("spravne.png").convert()
                imp = pygame.transform.scale(imp, (150, 45))
                self.solution_button = self.screen.blit(imp, (0, 410))

                self.update_level_and_score()
                time.sleep(0.5)

    def load_game(self):
        game_screen = self.screen.subsurface(self.rect_game)
        filepath = filepath = "mapa" + str(self.level_number) + ".txt"
        Game.initialize(filepath, game_screen)
        print('*', Game.has_solution)

        imp = pygame.image.load("neni_riesenia.png").convert()
        imp = pygame.transform.scale(imp, (150, 45))
        self.solution_button = self.screen.blit(imp, (0, 410))
        time.sleep(0.5)

    def update_level_and_score(self):
        self.screen.fill(pygame.Color("#D1A38C"), (30, 80, self.window_width, 40))
        score = 0
        for lvl in self.solved_level:
            if lvl:
                score+=1
        self.level_and_score = self.screen.blit(self.font.render('level '+str(self.level_number)+
        '   skóre:'+str(score)+'/10', True, (0, 50, 0)), (30, 80))
