import random

import pygame


class Field:
    def __init__(self, x, y):
        self._neighbours = []
        self._has_obstacle = False
        self._has_player = False
        self._visited = False
        self.color = (random.randint(10, 100), random.randint(10, 100), random.randint(10, 100))
        self.x = x
        self.y = y
        self.size = ...

    def draw(self, screen):
        from Game import Game
        block_size = Game.window_width // Game.max_x
        x_coord = self.x * block_size
        y_coord = self.y * block_size

        rect = pygame.Rect(x_coord, y_coord, block_size, block_size)
        color = self.color
        if self._visited:
            color = (200, 0, 0)
        if self._has_obstacle:
            color = (0, 0, 0)
        if self._has_player:
            color = (255, 255, 255)

        pygame.draw.rect(screen, color, rect)

    def add_neighbour(self, neighbour):
        self._neighbours.append(neighbour)

    def set_has_player(self, has_player):
        self._has_player = has_player
        self._visited = True

    def has_player(self):
        return self._has_player

    def set_has_obstacle(self, has_obstacle):
        self._has_obstacle = has_obstacle

    def has_obstacle(self):
        return self._has_obstacle

    def visited(self):
        return self._visited

    def __str__(self):
        return f"({self.x}, {self.y}) -> {len(self._neighbours)}; obstacle: {self.has_obstacle()};" \
               f" player: {self.has_player()}; visited: {self.visited()}"

    def __repr__(self):
        return self.__str__()
