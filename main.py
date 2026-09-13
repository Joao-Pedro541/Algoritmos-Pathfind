from executionWindow import window

import tkinter as tk

class app:
    def __init__(self):
        root = tk.Tk()
        root.title("Pathfind Test")
        root.geometry("320x375")
        root.resizable(False, False)

        self.height = 700
        self.width = 700
        self.gridTam = 10
        
        

        frame = tk.Frame(root)

        tk.Button(command=self.run, text="Run").pack(in_=frame,side=tk.LEFT)

        frame.pack()
        root.mainloop()

    def run(self):
        scene = window(self.gridTam,title="Pathfind Test",width=self.width,height=self.height)
        scene.run()

if __name__ == "__main__":
    app()
    