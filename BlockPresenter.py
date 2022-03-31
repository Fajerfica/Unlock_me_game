"""
Manage one block with BlockModel and BlockView
Karpenko Alice, K-12
"""


from BlockModel import BlockModel
from BlockView import BlockView
from BlockView import View


class BlockPresenter:
    def __init__(self, root_view: View, model: BlockModel, view: BlockView):
        """Compare BlockModel and BlockView"""

        self.model = model
        self.view = view
        self.view.show()
        self.root_view = root_view
        self._create_button_bind()

    def _create_button_bind(self):
        """Create bindings to canvas mouse click"""

        canvas = self.root_view.canvas()
        block_id = self.view._canvas_id
        canvas.tag_bind(block_id, "<Button-1>", self._mouse_click)

    def _arrow_event(self, event):
        """When arrow-key press this func do movings"""

        side = "<" + event.keysym + ">"
        if self.model.is_horisontal() == (side == "<Left>" or side == "<Right>"):
            (dx, dy) = self.model.get_shift_after_click(side)
            if not self.move(dx, dy):
                self._create_button_bind()

    def _mouse_click(self, event):
        """When mouse click, bind arrow-key press"""

        root = self.root_view.root()
        root.bind("<Left>", self._arrow_event)
        root.bind("<Right>", self._arrow_event)
        root.bind("<Up>", self._arrow_event)
        root.bind("<Down>", self._arrow_event)

    def move(self, dx, dy):
        """Make movings and checks"""

        self.view.hide()
        self.model.move(dx, dy)
        if self.model.end_game():
           self.root_view.end_game()
           self.end()
           end = True
        else:
            self.view.show()
            end = False

        return end

    def end(self):
        return True

    def show(self):
        """Start viewing"""

        self.root_view.show()
