class Player:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.path = [[x,y]]

    def move(self, new_x, new_y):
        from Game import Game
        if not self.can_move(new_x, new_y):
            return

        Game.fields[(self.x, self.y)].set_has_player(False)
        self.x = new_x
        self.y = new_y
        self.path.append([new_x, new_y])
        Game.fields[(new_x, new_y)].set_has_player(True)

    def can_move(self, new_x, new_y):
        from Game import Game
        if new_x < 0 or new_x >= Game.max_x:
            return False
        if new_y < 0 or new_y >= Game.max_y:
            return False
        if Game.fields[(new_x, new_y)].has_obstacle():
            return False
        if Game.fields[(new_x, new_y)].visited():
            return False

        return True

    def coordinates(self):
        return self.x, self.y

    def __repr__(self):
        return f"Player({self.x}, {self.y})"
