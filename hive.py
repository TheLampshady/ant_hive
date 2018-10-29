
CELL_SIZE = 4


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

    def console_log(self):
        size = len(self.board)
        # Top
        print("  ", end="")
        [print(" %02d  " % x, end="") for x in range(size)]
        print("")
        self.print_line(size)
        for i, x in enumerate(self.board):
            print("%02d|" % i, end="")
            line2 = [
                self.print_cell(y)
                for y in x
            ]
            print("\n  |", end="")
            [self.print_cell(y) for y in line2]
            print("")
            self.print_line(size)

    def print_cell(self, cell):
        if not cell:
            return print(" " * CELL_SIZE + "|", end="")

        if isinstance(cell, str):
            return print(cell[:CELL_SIZE] + "|", end="")

        entries = list(cell.items())
        print(self.format_cell(*entries[0]) + "|", end="")
        return self.format_cell(*entries[1]) if len(entries) > 1 else " " * CELL_SIZE

    def format_cell(self, key, val):
        if "ant" == key.lower():
            pass
        msg = key[0].upper() + str(val)[:CELL_SIZE-1]
        return msg + " " * (CELL_SIZE - len(msg))

    @staticmethod
    def print_line(len, char="-"):
        print("   ", end="")
        mod = int((CELL_SIZE + 1) * len) -1
        print(char * mod)
