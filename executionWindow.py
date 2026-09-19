import arcade

from objects import GridObject



class window(arcade.Window):

    def __init__(self,lengthGrid,typeExecution,pathfind,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.typeExecution = typeExecution
        self.pathfinder = pathfind
        self.objects = [GridObject(lengthGrid,self.width,self.height)]
        self.getfunction = lambda name,*args, **kwargs: [getattr(obj,name)(*args,**kwargs) for obj in self.objects if hasattr(obj, name)]
        self.objects.append(self.pathfinder(self.objects[0]))

    def on_update(self,delta_time):
        self.getfunction(self.typeExecution)
        return super().on_update(delta_time)
    
    def draw(self, dt):
        self.clear()
        self.getfunction("draw")
        return super().draw(dt)
    
    def on_mouse_press(self, x, y, button, modifiers):
        self.getfunction("on_mouse_press", x, y, button, modifiers)
        return super().on_mouse_press(x, y, button, modifiers)

    def on_key_press(self, symbol, modifiers):
        self.getfunction("on_press_key", symbol, modifiers)
        if symbol == arcade.key.ESCAPE:
            print("exit")
            self.close()
