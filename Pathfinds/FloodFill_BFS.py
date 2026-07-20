from objects import PathfindAlgoritm,BlockStates

class BFS(PathfindAlgoritm):
    def __init__(self, grid):
        self.startPath = False
        

        self.parent = {}
        self.verificy = []
        self.localizateEnd = False

        super().__init__(grid)
        self.ajustGrid()
        
        
    def ajustGrid(self):
        if self.gridObject is not None:
            self.START:tuple = self.gridObject.getBlock(state=BlockStates.START)
            self.END:tuple = self.gridObject.getBlock(state=BlockStates.END)

            if self.startPath == False and self.START in self.gridObject.blocks:
                self.parent = {}
                self.parent[self.START] = None
                self.verificy.clear()
                self.verificy.append(self.START)



    def returnPath(self,pos):
        path = []
        nodeActual = pos
        while nodeActual != self.START:
            path.append(nodeActual)
            nodeActual = self.parent[nodeActual]
        path.append(self.START)

        for b in path:
            if b not in (self.START, self.END):
                self.gridObject.setBlock(b, BlockStates.PATH)
        
        self.parent = {}
        

    def step(self):
        self.startPath = True
        for b in list(self.verificy):
            if self.localizateEnd == True:
                continue

            if b == self.END:
                self.continuoStep = False
                self.localizateEnd = True
                self.returnPath(b)
                continue
            
            neighbors = self.gridObject.getNeighbors(b, False)
            if neighbors == None:
                continue
            for n in neighbors:
                if n in self.gridObject.blocks:
                    if n in self.parent or self.gridObject.blocks[n] == BlockStates.WALL:
                        continue


                if self.gridObject.getBlock(b) != BlockStates.START and self.gridObject.getBlock(b) != BlockStates.END:
                    self.gridObject.setBlock(b,BlockStates.CLOSED)
                if self.gridObject.getBlock(n) != BlockStates.START and self.gridObject.getBlock(n) != BlockStates.END:
                    self.gridObject.setBlock(n,BlockStates.OPEN)

                self.parent[n] = b
                self.verificy.append(n)
            self.verificy.remove(b)
            

        return super().step()
    