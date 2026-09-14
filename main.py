from executionWindow import window

import tkinter as tk

class app:
    def __init__(self):
        root = tk.Tk()
        root.title("Pathfind Test")
        root.geometry("320x450")
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

        executeText = tk.Label(root,text="Execution Type")
        executeText.pack()

        self.executeType = tk.Listbox(root, selectmode=tk.SINGLE)
        self.executeType.pack()

        self.executeType.insert(1,"ExecuteOnce")
        self.executeType.insert(2,"step")
        frame = tk.Frame(root)

        tk.Button(command=self.run, text="Run").pack(in_=frame,side=tk.LEFT)

        frame.pack()
        root.mainloop()

    def run(self):
        scene = window(int(self.gridBox.get()), self.executeType.get(tk.ANCHOR), title="Pathfind Test", width=int(self.widthBox.get()), height=int(self.heightBox.get()))
        scene.run()



if __name__ == "__main__":
    app()
    