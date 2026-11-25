
import numpy as np
import cv2

from PIL import Image, ImageDraw

from .statesGrid import BlockStates


class GridRenderer:
    def __init__(self, grid, limityX, limityY):
        self.grid = grid
        self.img = Image.new(
            "RGBA",
            (limityX*2, limityY*2),
            color= (0,0,0,255)
        )

        self.frames = []


    def drawBlock(self, block, blocks):
        if block in blocks:
            color = self.grid.getColorBlock(blocks[block])
        else:
            color = self.grid.getColorBlock()

        draw = ImageDraw.Draw(self.img)
        draw.rectangle(
            (
                block[0],
                block[1],
                block[0] + self.grid.grid,
                block[1] + self.grid.grid
            ),
            fill=color
        )

    def render(self):
        if self.grid.newBlockDrawn == []:
            return None
        self.drawBlock(self.grid.newBlockDrawn[0], self.grid.blocks)
        self.grid.newBlockDrawn.remove(self.grid.newBlockDrawn[0])

        # Convertendo para NumPy
        frame = np.array(self.img)

        # PIL utiliza RGB, OpenCV normalmente utiliza BGR
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        return frame