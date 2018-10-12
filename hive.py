
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
        self.board = board
        self.id = board.get('id')
        if not self.id:
            raise LookupError("No Game ID")

        self.map = board.get('map')
        if not self.map:
            raise LookupError("No Game Map")

        self.ants = board.get('ants') or {}

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
