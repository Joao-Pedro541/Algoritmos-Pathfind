from enum import Enum,auto
import arcade 
import math


class BlockStates(Enum):
    START = auto()
    END = auto()

    EMPTY = auto()

    WALL = auto()

    OPEN = auto()
    CLOSED = auto()
    PATH = auto()

    CURRENT = auto()      # Nó sendo processado
    FRONTIER = auto()     # Opcional

class GridObject():
    def __init__(self,grid,limityX,limityY):
        self.grid = grid

        self.calcGrid = lambda x,y: ((x//self.grid)* self.grid,(y//self.grid)* self.grid)
        self.limity = (limityX,limityY)
 
        self.blocks = {
            self.calcGrid(0,0): BlockStates.START,
            self.calcGrid(690,690): BlockStates.END
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
        
    
    def ajustGrid(self):
        especialBlocks = {BlockStates.START: None,
                          BlockStates.END: None}
        for i in list(especialBlocks.keys()):
            for b in self.GetStates(i):
                print(i)
                if especialBlocks[i] is not None:
                    del self.blocks[especialBlocks[self.blocks[b]]]
                especialBlocks[i] = b

    def setBlock(self,block:tuple, state: BlockStates = BlockStates.EMPTY):
        if state == BlockStates.EMPTY:
            self.blocks.pop(block, None)
        elif (0,0) <= block < self.limity:
            self.blocks[self.calcGrid(*block)] = state



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
        
    def on_update(self,delta_time):
        pass
    def draw(self):
        for b in self.blocks:
            x,y = b
            arcade.draw_rect_filled(arcade.rect.XYWH(x +self.grid /2,y+self.grid /2,self.grid,self.grid),self.getColorBlock(self.blocks[b]))
    
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

        self.nextStep = False
        self.continuoStep = False
        
    def ajustGrid(self):
        pass

    def on_update(self,delta_time):
        self.ajustGrid()
        if self.nextStep or self.continuoStep:
            self.nextStep = False
            self.step()
    
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_MIDDLE:
            self.continuoStep = True
        
        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.nextStep = True

        

    def step(self):
        pass
