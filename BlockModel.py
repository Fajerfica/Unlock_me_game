"""
Logic of block movings
Karpenko Alice, K-12
"""

class BlockModel:

    _AREA_SIZE = 6

    def __init__(self, x1, y1, x2, y2, color, prisoner, main_model):
        """Create logic of movings"""

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self._prisoner = prisoner
        self.model = main_model
        main_model.set_rectangle(x1, y1, x2, y2, True)

    def move(self, dx, dy):
        """Create movings"""

        dx, dy = self.tuple1
        self.model.set_rectangle(self.x1, self.y1, self.x2, self.y2, False)
        self.x1 += dx
        self.x2 += dx
        self.y1 += dy
        self.y2 += dy
        if self.check_walls():
            self.model.set_rectangle(self.x1, self.y1, self.x2, self.y2, True)
        else:
            self.x1 -= dx
            self.x2 -= dx
            self.y1 -= dy
            self.y2 -= dy
            dx, dy = 0, 0
        return dx, dy

    def get_shift_after_click(self, side):
        """Function get side (arrow-key) and return how block shift depend on side and checking"""

        self.tuple = ()
        if side == "<Left>":
            self.tuple = (-1, 0)
        elif side == "<Right>":
            self.tuple = (1, 0)
        elif side == "<Up>":
            self.tuple = (0, -1)
        elif side == "<Down>":
            self.tuple = (0, 1)

        if self.model.checker(self.x1, self.y1, self.x2, self.y2, self.tuple[0], self.tuple[1]):
            self.tuple1 = self.tuple
        else:
            self.tuple1 = (0,0)
        return self.tuple1

    def check_walls(self):
        """Check collision with walls"""

        return 0 <= self.x1 < self._AREA_SIZE and 0 <= self.y1 < self._AREA_SIZE and 1 <= self.x2 <= self._AREA_SIZE \
                and 1 <= self.y2 <= self._AREA_SIZE

    def get_location(self):
        """Get location of block"""

        return self.x1, self.y1, self.x2, self.y2

    def end_game(self):
        """Check conditions for end game"""

        if self._prisoner:
            if self.get_location()[2] >= 6:
                return True

    def is_horisontal(self):
        """Check orientation of block"""
        return self.x2 - self.x1 > self.y2 - self.y1
