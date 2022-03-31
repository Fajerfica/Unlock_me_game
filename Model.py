"""
Check blocks overlappings
Karpenko Alice, K-12
"""

class Model:

    def __init__(self):
        """Check overlapping of blocks"""

        self.field = []
        self._init_field()

    def _init_field(self):
        """Make field of game"""

        self.field = [
            [False, False, False, False, False, False],
            [False, False, False, True, True, False],
            [False, True, True, True, True, False],
            [True, True, True, True, True, False],
            [False, True, False, False, False, False],
            [False, True, True, True, False, False]]
        n = 6
        self.field = [[False for i in range(n)] for j in range(n)]

    def set_rectangle(self, x1, y1, x2, y2, need_value):
        """Check where the rectangle is"""

        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                if y1 <= i < y2 and x1 <= j < x2:
                    self.field[i][j] = need_value

    def is_empty_rectangle(self, x1, y1, x2, y2):
        """Check empty sells"""

        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                if y1 <= i < y2 and x1 <= j < x2 and self.field[i][j]:
                    return False
        return True

    def checker(self, x1, y1, x2, y2, dx, dy):
        """Check blocks overlapping"""

        self.set_rectangle(x1, y1, x2, y2, False)
        check = self.is_empty_rectangle(x1 + dx, y1 + dy, x2 + dx, y2 + dy)
        self.set_rectangle(x1, y1, x2, y2, True)
        return check
