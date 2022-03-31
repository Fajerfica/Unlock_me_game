"""
Make root and canvas
Karpenko Alice, K-12
"""


from tkinter import *


class View:
    _CANVAS_WIDTH = 420
    _CANVAS_HEIGHT = 420
    _CANVAS_BACKGROUND_COLOR = '#CD853F'
    _WINDOW_TITLE = 'UNBLOCK ME'

    def __init__(self):
        """Make root and canvas for game and delete them in the end"""

        self._init_root()
        self._init_canvas()

    def _init_root(self):
        """Make root window"""

        self._root = Tk()
        self._root.title(self._WINDOW_TITLE)
        self._root.resizable(width=False, height=False)

    def _init_canvas(self):
        """Make canvas"""

        self._canvas = Canvas(self._root,
                              width=self._CANVAS_WIDTH,
                              height=self._CANVAS_HEIGHT,
                              background=self._CANVAS_BACKGROUND_COLOR)
        self._gate = self._canvas.create_rectangle(405, 140, 420, 210)
        self._canvas.pack()
        self._canvas.focus_set()

    def delete(self):
        """Destroy main window"""

        self._finish_root.destroy()

    def end_game(self):
        """Destroy main window and browse finish func"""

        self._root.destroy()

    def create_finish(self):
        """Create finish window"""

        self._finish_root = Tk()
        self._finish_root.title(self._WINDOW_TITLE)
        self._finish_root.resizable(width=False, height=False)
        l1 = Label(width=15, height=10, bg='#A0522D', text="The End")
        b1 = Button(width=15, height=10, bg='#A0522D', text="Exit", command=self.delete)
        b2 = Button(width=15, height=10, bg='#A0522D', text="Exit", command=self.restart)
        b2.pack()
        b1.pack()
        l1.pack()

    def restart(self):
        self._init_root()
        self._init_canvas()

    def canvas(self):
        canvas = self._canvas
        return canvas

    def root(self):
        root = self._root
        return root

    def show(self):
        """Start mainloop"""

        self._root.mainloop()
