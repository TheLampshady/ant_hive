from numbers import Number


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        elif isinstance(other, Number):
            return Point(self.x - other, self.y - other)
        raise ValueError("Invalid type: '%s'" % str(type(other)))

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, Number):
            return Point(self.x + other, self.y + other)
        raise ValueError("Invalid type: '%s'" % str(type(other)))

    def distance(self, other):
        if isinstance(other, Point):
            p = self - other
            return abs(p.x) + abs(p.y)
        raise ValueError("Invalid type: '%s'" % str(type(other)))

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
