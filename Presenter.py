"""
This file contains clas Presenter, which show start, main and finish windows
Karpenko Alice, K-12
"""

from BlockModel import BlockModel
from BlockView import BlockView
from BlockPresenter import BlockPresenter
from Model import Model
from View import View
from tkinter import *


class Presenter:
    _WINDOW_TITLE = "UnblockMe"

    def __init__(self):
        """Create blocks and start game"""

        self._list_blocks = dict()
        self.start_window()

    def _init_blocks(self):
        """Create blocks"""

        self.root_view = View()
        self.model = Model()
        model = self.model

        m1 = BlockModel(0, 3, 2, 4, "#A0522D", False, model)
        v1 = BlockView(m1, self.root_view)
        self._list_blocks[1] = BlockPresenter(self.root_view, m1, v1)

        m2 = BlockModel(1, 4, 2, 6, "#A0522D", False, model)
        v2 = BlockView(m2, self.root_view)
        self._list_blocks[2] = BlockPresenter(self.root_view, m2, v2)

        m3 = BlockModel(2, 3, 3, 5, "#A0522D", False, model)
        v3 = BlockView(m3, self.root_view)
        self._list_blocks[3] = BlockPresenter(self.root_view, m3, v3)

        m4 = BlockModel(2, 5, 4, 6, "#A0522D", False, model)
        v4 = BlockView(m4, self.root_view)
        self._list_blocks[4] = BlockPresenter(self.root_view, m4, v4)

        m5 = BlockModel(3, 1, 4, 4, "#A0522D", False, model)
        v5 = BlockView(m5, self.root_view)
        self._list_blocks[5] = BlockPresenter(self.root_view, m5, v5)

        m6 = BlockModel(4, 1, 5, 4, "#A0522D", False, model)
        v6 = BlockView(m6, self.root_view)
        self._list_blocks[6] = BlockPresenter(self.root_view, m6, v6)

        self._m7 = BlockModel(1, 2, 3, 3, "red", True, model)
        v7 = BlockView(self._m7, self.root_view)
        self._list_blocks[7] = BlockPresenter(self.root_view, self._m7, v7)

    def start_window(self):
        """ Create start window"""
        self._root = Tk()
        self._root.config(bg="#DEB887")
        self._root.title("UnblockMe")
        self._root.geometry("420x420+150+200")
        self._root.resizable(width=False, height=False)
        start_msg = Message(text="""\t\t\tHello, user!\n
            In this game you should unblock prisoner.\n
            Prisoner is red block. You can move blocks this way:
            click with mouse on block, which you want to move, after that
            press arrow-key, depend on side, where you want to move.\n
            Horizontal blocks you can move only left/right. 
            Vertical blocks you can move only up/down.
            End of the game, when you move prisoner to the gate.\n
           \t\t\tGood luck!!!""")
        start_msg.config(aspect="250", bg="#FFDEAD", fg="#6A5ACD")
        start_b = Button(bg='#CD853F', text="Start game", fg="white", font=("TkIconFont", 18),
                    command=self.start)
        exit_b = Button(bg='#FF6347', text="Exit", fg="white", font=("TkIconFont", 18),
                    command=self.exit)
        start_msg.pack()
        start_b.pack()
        exit_b.pack()
        self._root.mainloop()

    def exit(self):
        """Start exit method"""
        self._root.destroy()

    def start(self):
        """Start method"""
        self._root.destroy()
        self._init_blocks()

    def update_block(self):
        """Update block location and other things in game"""
        #self.root_view.show()
        for blocks in self._list_blocks.values():
            blocks.show()
        if self._list_blocks[7].end():
            self.create_finish()

    def create_finish(self):
        """Create finish window"""

        self._finish_root = Tk()
        self._finish_root.config(bg="#DEB887")
        self._finish_root.title(self._WINDOW_TITLE)
        self._finish_root.resizable(width=False, height=False)
        self._finish_root.geometry("420x420+200+200")
        end_message = Message(bg='#FFDEAD', text="""You win!!
        Congratulations, my dear!
        Do you want to restart?""", font=("TkTextFont", 18))
        end_message.config(aspect="250")
        restart_b = Button(bg='#CD853F', text="Restart", font=("TkIconFont", 18), command=self.restart)
        exit_b = Button(bg='#FF6347', text="Exit", font=("TkIconFont", 18), command=self.delete)
        end_message.pack()
        restart_b.pack()
        exit_b.pack()
        self._finish_root.mainloop()

    def delete(self):
        """Destroy main window"""

        self._finish_root.destroy()

    def restart(self):
        """Create new game"""
        self._finish_root.destroy()
        self._init_blocks()
        self.update_block()
