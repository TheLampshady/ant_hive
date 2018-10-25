import random

from hive import BaseHive
from .ant import Ant
from .food import Food
from .tools import Point

# ACTIONS = ["move", "eat", "load", "unload"]
# DIRECTIONS = ["up", "down", "right", "left"]


class MyHive(BaseHive):

    def __init__(self, board):
        super().__init__(board)
        self.hives = []
        self.foods = []
        self.all_ants = []

        self.my_ants = [Ant(key, value) for key, value in self.ants.items()]
        self.next_move = []
        self.output = {}
        self._load_board()

    # ------------------------ INIT ------------------------
    def _load_board(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j]:
                    self._process_cell(self.board[i][j], Point(i, j))

    def _process_cell(self, cell, point):
        if "hive" in cell:
            if cell['hive'] == self.id:
                self.hives.append(point)

        if "food" in cell:
            self.foods.append(
                Food(len(self.foods)+1, point, cell['food'])
            )

        if "ant" in cell:
            self.all_ants.append(point)

    # --------------------- Properties ---------------------
    @property
    def occupied(self):
        return self.hives + self.all_ants + self.next_move

    # --------------------- Process Game ---------------------

    def get_orders(self):
        hunt_ants = list(filter(lambda x: not x.has_food, self.my_ants))
        return_ants = list(filter(lambda x: x.has_food, self.my_ants))
        self.food_hunter(hunt_ants)
        self.return_hive(return_ants)
        return self.output

    def random(self):
        # Loop through ants and give random orders
        return {
            ant: {
                "act": self.ACTIONS[random.randint(0, 3)],
                "dir": self.DIRECTIONS[random.randint(0, 3)]
                }
            for ant in self.ants
        }

    def return_hive(self, return_ants):
        for ant in return_ants:
            hive = ant.pick_hive(self.hives)
            self.make_hive_move(ant, hive)

    def make_hive_move(self, ant, target):
        locs = ant.loc.steps(target)
        move = self.get_empty(locs, self.occupied)
        if move in self.hives:
            # Save new position
            self.next_move.append(ant.loc)
            self.output[ant.id] = dict(
                act=self.ACTIONS[3],
                dir=ant.loc.get_move_name(move)
            )
        else:
            self.next_move.append(move)
            self.output[ant.id] = dict(
                act=self.ACTIONS[0],
                dir=ant.loc.get_move_name(move)
            )

    def food_hunter(self, hunt_ants):
        foods = list(self.foods)
        count = min((len(hunt_ants)-1), len(foods))
        # Loop through each ant hunting. Last one picks last option
        for i in range(count):
            m = max(
                [(j, ant.pick_food(foods)) for j, ant in enumerate(hunt_ants)],
                key=lambda x: x[1]
            )
            ant = hunt_ants.pop(m[0])
            food = foods.pop(m[1][0])
            self.make_move(ant, food.loc)

        if foods and hunt_ants:
            ant = hunt_ants.pop(0)
            i = ant.pick_food(foods)[0] if len(foods) > 1 else 0
            food = foods.pop(i)
            self.make_move(ant, food.loc)

    def make_move(self, ant, target):
        locs = ant.loc.steps(target)
        move = self.get_empty(locs, self.occupied)
        food = Food.get_by_loc(move, self.foods)
        if food:
            # Remove move from map
            self.foods.remove(food)
            # Save new position
            self.next_move.append(ant.loc)
            self.output[ant.id] = dict(
                act=self.ACTIONS[2],
                dir=ant.loc.get_move_name(move)
            )
        else:
            self.next_move.append(move)
            self.output[ant.id] = dict(
                act=self.ACTIONS[0],
                dir=ant.loc.get_move_name(move)
            )

    @staticmethod
    def get_empty(locs, occupied):
        for loc in locs:
            if loc not in occupied:
                # TODO get boarders
                return loc
        return []





