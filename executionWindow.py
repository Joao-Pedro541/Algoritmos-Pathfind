import cv2
import numpy as np 

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
        out = cv2.VideoWriter(filename, fourcc, fps, (self.width * 2, self.height * 2))

        while True:

            frame = self.gridRenderer.render()
            if frame is None:
                break
            out.write(frame)

        print("Recording finished.")
        out.release()
        cv2.destroyAllWindows()

    def simulation(self):
        self.pathfinderObject.ExecuteOnce()

        self.record("output.mp4", fps=240)
        while True:
            start_time = time.time()
            frame = self.gridRenderer.render()
            if (cv2.waitKey(1) & 0xFF == ord('q') or frame is None):
                break
            cv2.imshow("Captured Frame", frame)
        cv2.destroyAllWindows() 


