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

        widthText = tk.Label(root,text="Width")
        widthText.pack()

        self.widthBox = tk.Entry(root)
        self.widthBox.pack()

        
        heightText = tk.Label(root,text="Height")
        heightText.pack()

        self.heightBox = tk.Entry(root)
        self.heightBox.pack()

        gridText = tk.Label(root,text="Grid Size")
        gridText.pack()

        self.gridBox = tk.Entry(root)
        self.gridBox.pack()
        
        frame = tk.Frame(root)

        tk.Button(command=self.run, text="Run").pack(in_=frame,side=tk.LEFT)

        frame.pack()
        root.mainloop()

    def run(self):
        scene = window(int(self.gridBox.get()),title="Pathfind Test",width=int(self.widthBox.get()),height=int(self.heightBox.get()))
        scene.run()



if __name__ == "__main__":
    app()
    