from enum import Enum,auto
import arcade 
import math

from PIL import Image, ImageDraw



class BlockStates(Enum):
    START = auto()
    END = auto()

    EMPTY = auto()

    WALL = auto()

    OPEN = auto()
    CLOSED = auto()
    PATH = auto()

    CURRENT = auto()
    FRONTIER = auto()

class GridObject():
    def __init__(self,grid,limityX,limityY):
        self.grid = grid

        self.calcGrid = lambda x,y: ((x//self.grid)* self.grid,(y//self.grid)* self.grid)
        self.limity = (limityX - self.grid,limityY - self.grid)
 
        self.blocks = {
            self.calcGrid(0,0): BlockStates.START,
            self.calcGrid(*self.limity): BlockStates.END
        }
        self.newBlockDrawn = {
            self.calcGrid(0,0): BlockStates.START,
            self.calcGrid(*self.limity): BlockStates.END
        }
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

        self.img = Image.new("RGBA", (limityX, limityY), color=arcade.color.BLACK)
        self.drawImg = arcade.Sprite(self.img, center_x=limityX//2, center_y=limityY//2)

        print(self.img)
        print(self.drawImg)
        
    
    def ajustGrid(self):
        especialBlocks = {BlockStates.START: None,
                          BlockStates.END: None}
        for i in list(especialBlocks.keys()):
            for b in self.GetStates(i):
                if especialBlocks[i] is not None:
                    del self.blocks[especialBlocks[self.blocks[b]]]
                especialBlocks[i] = b

    def setBlock(self,block:tuple, state: BlockStates = BlockStates.EMPTY):
        if state == BlockStates.EMPTY:
            self.blocks.pop(block, None)
        if (0,0) <= block < self.limity:
            self.blocks[self.calcGrid(*block)] = state
            self.newBlockDrawn[self.calcGrid(*block)] = state

    def drawBlock(self,block:tuple):
        print(block)
        color = None
        if block in self.blocks:
            color = self.getColorBlock(self.blocks[block])
        else:
            color = self.getColorBlock(BlockStates.EMPTY)
        draw = ImageDraw.Draw(self.img)
        draw.rectangle((block[0], block[1], block[0] + self.grid, block[1] + self.grid), fill=color)
        self.newBlockDrawn.pop(block, None)



    def getBlock(self, block:tuple = None,  state: BlockStates = None):
        if block is not None:
            if block in self.blocks:
                return self.blocks[block] 
        
        if state is not None:
            for pos, s in self.blocks.items():
                if s == state:
                    return pos
                
    def GetStates(self,state: BlockStates = None):
        if state is not None:
            blocksStates = []
            for pos, s in self.blocks.items():
                if s == state:
                    blocksStates.append(pos)
            return blocksStates

    def on_update(self,delta_time):
        print("update")
        for b in list(self.newBlockDrawn.keys()):
            self.drawBlock(b)

        self.drawImg.texture = arcade.Texture(self.img)
    
    def getNeighbors(self,pos:tuple,diagonal = True):
        if pos not in self.blocks:
            return None
        
        neightbors = {}

        for x in range(int(pos[0] - self.grid),int(pos[0] + self.grid*2),int(self.grid)):
            for y in range(int(pos[1] - self.grid),int(pos[1] + self.grid*2),int(self.grid)):
                if (x, y) == pos:
                    continue

                dx = x == pos[0]
                dy = y == pos[1]
                if not diagonal and not (dx or dy):
                    continue
                if (x,y) in self.blocks:
                    neightbors[(x,y)] = self.blocks[(x,y)]
                    continue
                neightbors[(x,y)] = BlockStates.EMPTY
        if neightbors == {}:
            return None
        return neightbors
            
    def getColorBlock(self,state = BlockStates.EMPTY):
        return self.block_colors[state]
    
    def on_draw(self):
        arcade.draw_sprite(self.drawImg)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            mousePos = self.calcGrid(x,y)

            if mousePos in self.blocks:
                self.setBlock(mousePos,BlockStates(self.blocks[mousePos].value + 1 if self.blocks[mousePos].value < 4 else 1))
            else:
                self.setBlock(mousePos,BlockStates.WALL)

            self.ajustGrid()
                
class PathfindAlgoritm():
    def __init__(self,grid:GridObject):
        self.gridObject = grid

        self.START:tuple = None
        self.END:tuple = None

        self.ajustGrid()
        
    def ajustGrid(self):
        pass

    def on_update(self,delta_time):
        pass

    def ExecuteOnce(self):
        pass

    def step(self):
        pass