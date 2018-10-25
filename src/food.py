
class Food(object):

    def __init__(self, key, loc, value):
        super().__init__()
        self.id = int(key)
        self.value = value
        self.loc = loc

    @classmethod
    def get_by_loc(cls, point, foods):
        for i, food in enumerate(foods):
            if point == food.loc:
                return food

        return None

    def __eq__(self, other):
        return self.id == other.id and self.loc == other.loc
