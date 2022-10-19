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
    mode = "test"

    player = None
    has_solution = None
    screen = None

    total_number_of_free_fields = 0

    @classmethod
    def initialize(cls, file_path, screen):
        cls.screen = screen
        cls.screen.fill((0, 0, 0))

        cls.load_game(file_path)

        cls.total_number_of_free_fields = 0
        for field in cls.fields.values():
            if not field._has_obstacle:
                cls.total_number_of_free_fields += 1

        print(cls.total_number_of_free_fields)


    @classmethod
    def load_game(cls, file_path):
        with open(file_path, 'r') as file:
            for index, line in enumerate(file):
                if index == 0:
                    max_x, max_y = [int(e) for e in line.split(" ")]
                    Game.initialize_fields(max_x, max_y)
                    Game.max_y, Game.max_x = max_y, max_x
                    continue
                if index == 1:
                    x, y = [int(e) for e in line.split(" ")]
                    Game.fields[(x, y)].set_has_player(True)
                    cls.player = Player(x, y)
                    continue
                if index == 2:
                    cls.has_solution = True if line.strip() == 'True' else False
                    print(cls.has_solution)
                    print(line)
                    continue
                x, y = [int(e) for e in line.split(" ")]
                Game.fields[(x, y)].set_has_obstacle(True)
        print("loaded")

    @staticmethod
    def initialize_fields(max_x, max_y):
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

    @classmethod
    def main_loop(cls):
        cls.draw_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(cls.fields)
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                x, y = cls.player.coordinates()
                new_x, new_y = x, y
                if event.key == pygame.K_LEFT:
                    new_x = x - 1
                if event.key == pygame.K_RIGHT:
                    new_x = x + 1
                if event.key == pygame.K_UP:
                    new_y = y - 1
                if event.key == pygame.K_DOWN:
                    new_y = y + 1
                cls.player.move(new_x, new_y)
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                if 5 < pos[0] < 180 and 410 < pos[1] < 430:
                    continue
                block_size = Game.window_width // Game.max_x
                x = (pos[0] - 150) // block_size
                y = (pos[1] - 150) // block_size
                if (x, y) in Game.fields and not Game.fields[(x, y)].has_player():
                    Game.fields[(x, y)].on_click()
                    pygame.display.update()

    @classmethod
    def draw_grid(cls):
        for x in range(Game.max_x):
            for y in range(Game.max_y):
                Game.fields[(x, y)].draw(cls.screen)
        pygame.display.update()

    @classmethod
    def check_hamilton(cls):
        begin_v = cls.fields[(0,0)]

        number_of_fields_without_obstacles = 0
        for field in cls.fields.values():
            if not field.has_obstacle():
                number_of_fields_without_obstacles += 1

        print(number_of_fields_without_obstacles)
        visited = set()
        
        def backtrack(beg_v):
            visited.add(beg_v)
            if len(visited) == number_of_fields_without_obstacles:
                return True

            for v in beg_v._neighbours:
                if v in visited or v.has_obstacle():
                    continue
                if backtrack(v):
                    return True

            visited.remove(beg_v)
            return False

        return backtrack(begin_v)

    @classmethod
    def save_as_file(cls, name, has_solution):
        with open(name, 'w') as file:
            file.write(str(cls.max_x) + " " + str(cls.max_y) + "\n")
            file.write(str(0) + " " + str(0) + "\n")
            file.write(str(has_solution) + "\n")
            for x in range(Game.max_x):
                for y in range(Game.max_y):
                    if Game.fields[(x, y)].has_obstacle():
                        file.write(str(x) + " " + str(y) + "\n")


