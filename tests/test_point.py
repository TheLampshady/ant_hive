from tests.base import BaseTest

from src.tools import Point


class TestPoint(BaseTest):

    def test_point(self):
        p = Point(0, 1)
        self.assertEqual(0, p.x)
        self.assertEqual(1, p.y)

    def test_point_ops(self):
        p = Point(0, 1)
        p2 = Point(2, 3)
        p3 = p + p2
        self.assertEqual(0, p.x)
        self.assertEqual(1, p.y)
        self.assertEqual(2, p2.x)
        self.assertEqual(3, p2.y)
        self.assertEqual(2, p3.x)
        self.assertEqual(4, p3.y)

        self.assertEqual(p, p3 - p2)

    def test_point_distance(self):
        p = Point(0, 1)
        x = p.distance(Point(2, 3))
        self.assertEqual(4, x)