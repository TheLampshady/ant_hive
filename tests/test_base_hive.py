import json

from tests.base import BaseTest
from tests.mock import get_simple

from src.my_hive import MyHive
from src.tools import Point


class TestBaseHive(BaseTest):

    def test_hive(self):
        payload = get_simple()
        hive = MyHive(payload)
        self.assertTrue(hive)

    def test_board_loads(self):
        payload = self.load_json("15x15.json")
        hive = MyHive(payload)
        self.assertEqual(15, hive.width)
        self.assertEqual(15, hive.height)

    def test_board_prints(self):
        payload = self.load_json("15x15.json")
        hive = MyHive(payload)
        hive.console_log()