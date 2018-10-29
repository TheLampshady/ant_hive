from .tools import Point


class Ant(object):

    def __init__(self, key, props=None):
        super().__init__()
        self.id = int(key)
        if not props:
            props = dict()

        self.age = int(props.get('age', 0))
        self.payload = int(props.get('payload', 0))
        self.wasted = int(props.get('wasted', 0))
        self.event = props.get('event', 0)
        self.loc = self.set_loc(props)

    @staticmethod
    def set_loc(props):
        x = props.get('x', 0)
        y = props.get('y', 0)
        return Point(int(x), int(y))

    @property
    def has_food(self):
        return bool(self.payload)

    def move(self, action):
        pass

    def food_score(self, food):
        return food.value / self.loc.distance(food.loc)

    def pick_food(self, foods):
        if not foods:
            return None, None
        scores = [
            (i, self.food_score(food))
            for i, food in enumerate(foods or [])
        ]
        return max(scores, key=lambda x: x[1])

    def pick_hive(self, hives):
        scores = [
            (hive, self.loc.distance(hive))
            for hive in hives or []
        ]
        return min(scores, key=lambda x: x[1])[0]
