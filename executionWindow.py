import cv2
import numpy as np 
import tkinter as tk

import time

from SystemGrid.GridObject import GridClass
from SystemGrid.RenderObject import GridRenderer

class window:

    def __init__(self,lengthGrid,pathfind,width,height):

        self.width = width
        self.height = height

        self.pathfinder = pathfind
        self.gridObject = GridClass(lengthGrid,self.width,self.height)

        self.gridRenderer = GridRenderer(self.gridObject, self.width, self.height)
        self.pathfinderObject = self.pathfinder(self.gridObject)

        self.simulation()

    def record(self, filename, fps=30):
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(filename, fourcc, fps, (self.width, self.height))

        while True:

            frame = self.gridRenderer.render()
            if frame is None:
                break
            out.write(frame)

        print("Recording finished.")
        out.release()
        cv2.destroyAllWindows()

    def simulation(self):
        self.pathfinderObject.run()

        root = tk.Tk()
        root.title("videoPathfind")
        root.geometry("320x320")
        root.resizable(False, False)
        tkFrame = tk.Frame(root)
        
        pause = False

        frameInt = 0
        show = True

        while show:
            
            frame = self.gridRenderer.render(frameInt)
            if frame is not None:
                cv2.imshow("Pathfind Simulation", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    pause = not pause
                if cv2.waitKey(1) & 0xFF == ord('e'):
                    break
            else:
                show = False

            frameInt = frameInt + 1 if not pause or len(self.gridObject.newBlockDrawn) <= frameInt else len(self.gridObject.newBlockDrawn) - 1
        self.record("output.mp4", fps=30)


