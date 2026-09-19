from executionWindow import window

import tkinter as tk
from tkinter import filedialog 

import importlib.util as lib_util

def returnPathfinder(path, module_name = "pathfind"):
    spec = lib_util.spec_from_file_location(module_name, path)
    module = lib_util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, module_name)
class app:
    def __init__(self):
        root = tk.Tk()
        root.title("Pathfind Test")
        root.geometry("320x600")
        root.resizable(False, False)

        self.height,self.width,self.gridTam = None,None,None

        tk.Label(root,text="Width").pack()

        self.widthBox = tk.Entry(root)
        self.widthBox.pack()

        
        tk.Label(root,text="Height").pack()

        self.heightBox = tk.Entry(root)
        self.heightBox.pack()

        gridText = tk.Label(root,text="Grid Size")
        gridText.pack()

        self.gridBox = tk.Entry(root)
        self.gridBox.pack()

        tk.Label(root,text="Execution Type").pack()

        self.executeType = tk.Listbox(root, selectmode=tk.SINGLE)
        self.executeType.pack()

        self.executeType.insert(1,"ExecuteOnce")
        self.executeType.insert(2,"step")
        frame = tk.Frame(root)

        tk.Label(root,text="File Selected").pack()
        
        self.pathfinderPath = tk.Entry(root)
        self.pathfinderPath.pack()
        self.pathfinderPath.insert(0, "No file loaded")
        tk.Button(command=self.openFile, text="Load Pathfinder Path").pack()

        

        tk.Label(root,text="Module Name").pack()

        self.nameModule = tk.Entry(root)
        self.nameModule.pack()

        tk.Label(root,text="Execution").pack()
        tk.Button(command=self.run, text="Run").pack(in_=frame,side=tk.LEFT)

        frame.pack()
        root.mainloop()

    def run(self):
        try:
            pathfinder_class = returnPathfinder(self.pathfinderPath.get(), self.nameModule.get())
            scene = window(int(self.gridBox.get()), self.executeType.get(tk.ANCHOR),pathfinder_class,title="Pathfind Test", width=int(self.widthBox.get()), height=int(self.heightBox.get()))
            scene.run()
        except ValueError:
            warning = tk.Tk()
            warning.title("Error")
            warning.geometry("200x100")
            tk.Label(warning, text="Please fill in all fields with valid values.", wraplength=180, justify=tk.LEFT).pack(padx=10, pady=10, fill=tk.X)
            warning.mainloop()
            warning.mainloop()
        except Exception as e:
            warning = tk.Tk()
            warning.title("Error")
            warning.geometry("200x100")
            tk.Label(warning, text=f"Error: {e}", wraplength=180, justify=tk.LEFT).pack(padx=10, pady=10, fill=tk.X)
            warning.mainloop()

    def openFile(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if file_path:
            self.pathfinderPath.delete(0, tk.END)
            self.pathfinderPath.insert(0, file_path)
            print(f"Loaded pathfinder file: {file_path}")

if __name__ == "__main__":
    app()
    