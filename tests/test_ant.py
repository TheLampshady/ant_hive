from tests.base import BaseTest

from src.ant import Ant, Point
from src.food import Food


class TestAnt(BaseTest):

    def test_ant(self):
        key = 1
        props = {
              "wasted": 3,
              "age": 38,
              "health": 8,
              "payload": 3,
              "x": 3,
              "y": 2,
              "event": "good"
        }

        ant = Ant(key, props)
        self.assertTrue(ant)
        self.assertEqual(38, ant.age)
        self.assertEqual(Point(3, 2), ant.loc)

    def test_ant_food_score(self):
        fp = Point(1, 2)
        f = Food(1, fp, 4)

        ant = Ant(1)
        ant.loc = Point(0, 0)
        self.assertAlmostEqual(1.333, ant.food_score(f), 3)

    def test_ant_pick_food(self):
        foods = [Food(1, Point(1, x), x + 2) for x in range(4)]
        ant = Ant(1)
        ant.loc = Point(0, 0)
        i = ant.pick_food(foods)
        self.assertEqual(0, i[0])
        self.assertEqual(2.0, i[1])