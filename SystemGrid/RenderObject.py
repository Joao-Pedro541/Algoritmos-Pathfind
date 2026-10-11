
import arcade
from PIL import Image, ImageDraw

from .statesGrid import BlockStates


class GridRenderer:
    def __init__(self, grid, limityX, limityY):
        self.grid = grid
        self.img = Image.new(
            "RGBA",
            (limityX, limityY),
            color=arcade.color.BLACK
        )
        self.drawImg = arcade.Sprite(
            self.img,
            center_x=limityX // 2,
            center_y=limityY // 2
        )

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

    def on_update(self, delta_time):
        for b in list(self.grid.newBlockDrawn):
            self.drawBlock(b, self.grid.blocks)
            self.grid.newBlockDrawn.remove(b)

        self.drawImg.texture = arcade.Texture(self.img)

    def on_draw(self):
        arcade.draw_sprite(self.drawImg)
