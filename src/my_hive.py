import random

from hive import BaseHive
from .tools import Point

# ACTIONS = ["move", "eat", "load", "unload"]
# DIRECTIONS = ["up", "down", "right", "left"]


class MyHive(BaseHive):

    def __init__(self, board):
        super().__init__(board)
        self.hives = []
        self.foods = []
        self.all_ants = []

    def get_orders(self):
        return self.random()

    def random(self):
        # Loop through ants and give random orders
        return {
            ant: {
                "act": self.ACTIONS[random.randint(0, 3)],
                "dir": self.DIRECTIONS[random.randint(0, 3)]
                }
            for ant in self.ants
        }

    def hunt(self):
        pass

    def _get_items(self, item):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j]:
                    self._process_cell(self.board[i][j], Point(i, j))

    def _process_cell(self, cell, point):
        if "hive" in cell:
            if cell['hive'] == self.id:
                self.hives.append(point)

        if "food" in cell:
            self.foods.append((point, cell['food']))

        if "ant" in cell:
            self.all_ants.append(point)
