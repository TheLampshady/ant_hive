
class BaseHive(object):
    ACTIONS = ["move", "eat", "load", "unload"]
    DIRECTIONS = ["up", "down", "right", "left"]

    def __init__(self, board):
        """
        Game description
        :type board: dict
            :properties: 'id' | Game id
            :properties: 'ants' | Dict of ants and stats
            :properties: 'map' | Dict of board objects
        """
        self.id = board.get('id')
        self.map = board.get('map')
        if not self.map:
            raise LookupError("No Game Map")

        self.ants = board.get('ants') or {}

        self.width = self.map.get("width")
        self.height = self.map.get("height")
        self.board = self.map.get("cells")
        self._validate()

    def _validate(self):
        if not self.id:
            raise LookupError("No Game ID")
        if not self.width or not self.height:
            raise ValueError("Board requires spaces")

        if self.height != len(self.board):
            raise ValueError("Board height doesnt match")

        for row in self.board:
            if self.width != len(row):
                raise ValueError("Board width doesnt match")

    @classmethod
    def process(cls, game_state):
        """
        Options for running one liner.
        :rtype game_state: dict
        :rtype: dict | for json response
        """
        return cls(game_state).get_orders()

    def get_orders(self):
        """

        :rtype: dict |
            :key: str with ant ID,
            :value: {"act": .., "dir": ..}
        """
        raise NotImplementedError
