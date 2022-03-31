"""
Create view of blocks
Karpenko Alice, K-12
"""

from View import View
from BlockModel import BlockModel

class BlockView():
    _cell_size = 70

    def __init__(self, block: BlockModel, root_view: View):
        """Create block on Canvas"""
        self._block = block
        self._canvas_id = None
        self.root_view = root_view

    def show(self):
        """Create rectangles with block coords"""

        x1 = self._block.x1 * self._cell_size
        x2 = self._block.x2 * self._cell_size
        y1 = self._block.y1 * self._cell_size
        y2 = self._block.y2 * self._cell_size
        color = self._block.color

        self._canvas_id = self.root_view.canvas().create_rectangle(
            x1, y1, x2, y2, fill=color,
            activefill="white", outline='#CD853F', width='2')

    def hide(self):
        """Delete rectangle-block"""
        
        self.root_view.canvas().delete(self._canvas_id)
        self._canvas_id = None
