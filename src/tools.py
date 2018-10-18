from numbers import Number


def validate(func):
    def wrapper(*args, **kwargs):
        if not isinstance(args[1], Point):
            raise ValueError("Invalid type: '%s'" % str(type(args[0])))
        return func(*args, **kwargs)
    return wrapper


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

    @validate
    def distance(self, other):
        p = self - other
        return abs(p.x) + abs(p.y)

    @validate
    def closer(self, other):
        p = self - other
        return abs(p.x) + abs(p.y)

    @validate
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
