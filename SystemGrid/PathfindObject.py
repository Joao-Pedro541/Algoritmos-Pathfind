from .GridObject import GridClass

class PathfindAlgoritm():
    def __init__(self,grid:GridClass):
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