import arcade

from objects import GridObject
from Pathfinds.FloodFill_BFS import BFS


class window(arcade.Window):

    def __init__(self,lengthGrid,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.objects = [GridObject(lengthGrid,self.height,self.width)]
        self.getfunction = lambda name,*args, **kwargs: [getattr(obj,name)(*args,**kwargs) for obj in self.objects if hasattr(obj, name)]
        self.objects.append(BFS(self.objects[0]))

    def on_update(self,delta_time):
        self.getfunction("on_update",delta_time)
        return super().on_update(delta_time)
    
    def draw(self, dt):
        self.clear()
        self.getfunction("draw")
        return super().draw(dt)
    
    def on_mouse_press(self, x, y, button, modifiers):
        self.getfunction("on_mouse_press", x, y, button, modifiers)
        return super().on_mouse_press(x, y, button, modifiers)


if __name__ == "__main__":

    heigth = int(input("how is the height:"))
    width = int(input("how is the width:"))
    gridTam = int(input("how grid space:"))

    scene = window(gridTam,title="Pathfind Test",width=width,height=heigth)
    scene.run()