from .GridObject import GridClass

class PathfindAlgoritm():
    def __init__(self,grid:GridClass):
        self.gridObject = grid

        self.START:tuple = None
        self.END:tuple = None

        self.ajustGrid()

    def ajustGrid(self):
        pass

    def run(self):
        pass
    def step(self):
        pass