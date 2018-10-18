
class Food(object):

    def __init__(self, key, loc, value):
        super().__init__()
        self.id = int(key)
        self.value = value
        self.loc = loc
