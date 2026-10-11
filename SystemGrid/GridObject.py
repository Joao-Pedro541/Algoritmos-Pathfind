
import arcade

from .statesGrid import BlockStates
from .RenderObject import GridRenderer


class GridClass:
    def __init__(self, grid: int, limityX: int, limityY: int):
        self.grid = grid

        self.calcGrid = lambda x, y: (
            (x // self.grid) * self.grid,
            (y // self.grid) * self.grid
        )
        self.limity = (limityX - self.grid, limityY - self.grid)

        self.blocks = {
            self.calcGrid(0, 0): BlockStates.START,
            self.calcGrid(*self.limity): BlockStates.END
        }
        self.newBlockDrawn = [
            self.calcGrid(0, 0),
            self.calcGrid(*self.limity)
        ]

        self.block_colors = {
            BlockStates.EMPTY: arcade.color.BLACK,
            BlockStates.START: arcade.color.DARK_GREEN,
            BlockStates.END: arcade.color.RED,
            BlockStates.WALL: arcade.color.DARK_BLUE,

            BlockStates.OPEN: arcade.color.LIME_GREEN,
            BlockStates.CLOSED: arcade.color.CYAN,
            BlockStates.PATH: arcade.color.GOLD,

            BlockStates.CURRENT: arcade.color.ORANGE,
            BlockStates.FRONTIER: arcade.color.CYAN,
        }

    def ajustGrid(self):
        especialBlocks = {
            BlockStates.START: None,
            BlockStates.END: None
        }
        for i in list(especialBlocks.keys()):
            for b in self.GetStates(i):
                if especialBlocks[i] is not None:
                    del self.blocks[especialBlocks[self.blocks[b]]]
                especialBlocks[i] = b

    def setBlock(self, block: tuple, state: BlockStates = BlockStates.EMPTY):
        if state == BlockStates.EMPTY:
            self.blocks.pop(block, None)
        if (0, 0) <= block < self.limity:
            self.blocks[self.calcGrid(*block)] = state
        self.newBlockDrawn.append(block)

    def getBlock(self, block: tuple = None, state: BlockStates = None):
        if block is not None:
            if block in self.blocks:
                return self.blocks[block]

        if state is not None:
            for pos, s in self.blocks.items():
                if s == state:
                    return pos

    def GetStates(self, state: BlockStates = None):
        if state is not None:
            blocksStates = []
            for pos, s in self.blocks.items():
                if s == state:
                    blocksStates.append(pos)
            return blocksStates

    def getNeighbors(self, pos: tuple, diagonal=True):
        if pos not in self.blocks:
            return None

        neightbors = {}

        for x in range(
            int(pos[0] - self.grid),
            int(pos[0] + self.grid * 2),
            int(self.grid)
        ):
            for y in range(
                int(pos[1] - self.grid),
                int(pos[1] + self.grid * 2),
                int(self.grid)
            ):
                if (x, y) == pos:
                    continue

                dx = x == pos[0]
                dy = y == pos[1]

                if not diagonal and not (dx or dy):
                    continue

                if (x, y) in self.blocks:
                    neightbors[(x, y)] = self.blocks[(x, y)]
                    continue

                neightbors[(x, y)] = BlockStates.EMPTY

        if neightbors == {}:
            return None

        return neightbors

    def getColorBlock(self, state=BlockStates.EMPTY):
        return self.block_colors[state]

