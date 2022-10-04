import random

import pygame

green_palette = ['#344c11', '#778d45', '#5c7c24', '#9ec650', '#20a447']

class Field:
    def __init__(self, x, y):
        self._neighbours = []
        self._has_obstacle = False
        self._has_player = False
        self._visited = False
        self.color = random.choice(green_palette)
        # yellow shades
        self._viscolor = (random.randint(245, 255), random.randint(226, 255), random.randint(30, 103))
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
            color = self._viscolor

        if self._has_obstacle:
            imp = pygame.image.load("hribik.png").convert()
            imp = pygame.transform.scale(imp, (block_size, block_size))
            screen.blit(imp, (x_coord, y_coord, block_size, block_size))
            return

        if self._has_player:
 
            # create a surface object, image is drawn on it.
            imp = pygame.image.load("slimak.png").convert()
            imp = pygame.transform.scale(imp, (block_size, block_size))
            screen.blit(imp, (x_coord, y_coord, block_size, block_size))
            return

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
