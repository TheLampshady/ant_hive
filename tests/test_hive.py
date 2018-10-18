import json

from tests.base import BaseTest
from tests.mock import get_simple

from src.my_hive import MyHive
from src.tools import Point


class TestHive(BaseTest):

    def test_hive(self):
        payload = get_simple()
        hive = MyHive(payload)
        self.assertTrue(hive)

    def test_board_loads(self):
        payload = self.load_json("15x15.json")
        hive = MyHive(payload)
        self.assertEqual(15, hive.width)
        self.assertEqual(15, hive.height)

    def test_board_loads_hives(self):
        payload = self.load_json("15x15.json")
        hive = MyHive(payload)

        self.assertEqual(4, len(hive.hives))
        self.assertIn(Point(0, 2), hive.hives)
        self.assertIn(Point(0, 3), hive.hives)
        self.assertIn(Point(0, 4), hive.hives)
        self.assertIn(Point(1, 3), hive.hives)

    def test_board_loads_food(self):
        payload = self.load_json("15x15.json")
        hive = MyHive(payload)

        self.assertEqual(20, len(hive.foods))
        expected = [
            (Point(11, 6), 9),
            (Point(1, 12), 5)
        ]

        points = [x.loc for x in hive.foods]
        for p, f in expected:
            i = points.index(p)
            self.assertTrue(i >= 0)
            self.assertEqual(f, hive.foods[i].value)
