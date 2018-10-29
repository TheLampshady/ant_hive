from numbers import Number


def validate(func):
    def wrapper(*args, **kwargs):
        if not isinstance(args[1], Point):
            raise ValueError("Invalid type: '%s'" % str(type(args[1])))
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
    def steps(self, other):
        if self == other:
            return []
        result = []
        mod_x = self._get_step(other.x, self.x)
        mod_y = self._get_step(other.y, self.y)

        # Forward
        if mod_x:
            result.append(Point(self.x + mod_x, self.y))
        if mod_y:
            result.append(Point(self.x, self.y + mod_y))

        # Sideways
        if not mod_x:
            result.append(Point(self.x + 1, self.y))
            result.append(Point(self.x - 1, self.y))

        if not mod_y:
            result.append(Point(self.x, self.y + 1))
            result.append(Point(self.x, self.y - 1))

        # Backwards
        if mod_x:
            result.append(Point(self.x - mod_x, self.y))
        if mod_y:
            result.append(Point(self.x, self.y - mod_y))
        return result

    def get_move_name(self, other):
        if self == other:
            return None
        if self.x != other.x:
            return "LEFT" if self.x > other.x else "RIGHT"
        return "UP" if self.x > other.x else "DOWN"

    @validate
    def is_between(self, other):
        """
        Is point between other and 0,0
        :param other: Point
        :rtype: Boolean
        """
        return 0 <= self.x < other.x and 0 <= self.y < other.y

    @staticmethod
    def _get_step(x, y):
        if x == y:
            return 0
        return 1 if x > y else -1

    @validate
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
