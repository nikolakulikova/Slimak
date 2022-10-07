import sys

import pygame

from Field import Field
from Player import Player


class Game:
    fields = dict()
    max_x = 0
    max_y = 0
    window_width = 450
    window_height = 450

    def __init__(self, file_path, screen):
        self.player = None
        self.has_solution = True

        # key: (x, y), value: Field
        self.load_game(file_path)

        # Pygame stuff
        self.screen = screen
        self.screen.fill((0, 0, 0))


    def load_game(self, file_path):
        with open(file_path, 'r') as file:
            for index, line in enumerate(file):
                if index == 0:
                    max_x, max_y = [int(e) for e in line.split(" ")]
                    self.initialize_fields(max_x, max_y)
                    Game.max_y, Game.max_x = max_y, max_x
                    continue
                if index == 1:
                    x, y = [int(e) for e in line.split(" ")]
                    Game.fields[(x, y)].set_has_player(True)
                    self.player = Player(x, y)
                    continue
                if index == 2:
                    self.has_solution = line
                    continue
                x, y = [int(e) for e in line.split(" ")]
                Game.fields[(x, y)].set_has_obstacle(True)
        print("loaded")

    def initialize_fields(self, max_x, max_y):
        Game.fields = dict()
        for x in range(max_x):
            for y in range(max_y):
                Game.fields[(x, y)] = Field(x, y)
        for x in range(max_x):
            for y in range(max_y):
                for delta_x in [-1, 0, 1]:
                    for delta_y in [-1, 0, 1]:
                        # diagonal stuff
                        if abs(delta_x) + abs(delta_y) == 2:
                            continue
                        new_x, new_y = x + delta_x, y + delta_y
                        if new_x == x and new_y == y:
                            continue
                        if new_x < 0 or new_x >= max_x or new_y < 0 or new_y >= max_y:
                            continue
                        Game.fields[(x, y)].add_neighbour(Game.fields[(new_x, new_y)])

    def main_loop(self):
        while True:
            self.draw_grid()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print(self.fields)
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    x, y = self.player.coordinates()
                    new_x, new_y = x, y
                    if event.key == pygame.K_LEFT:
                        new_x = x - 1
                    if event.key == pygame.K_RIGHT:
                        new_x = x + 1
                    if event.key == pygame.K_UP:
                        new_y = y - 1
                    if event.key == pygame.K_DOWN:
                        new_y = y + 1
                    self.player.move(new_x, new_y)
            pygame.display.update()

    def draw_grid(self):
        for x in range(Game.max_x):
            for y in range(Game.max_y):
                Game.fields[(x, y)].draw(self.screen)

    def check_hamilton(self):
        #ToDo nejaka logika grafov
        ...
