import random

from hive import BaseHive


class MyHive(BaseHive):

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
