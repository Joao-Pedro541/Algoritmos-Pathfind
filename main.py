from executionWindow import window


if __name__ == "__main__":

    height = int(input("how is the height:"))
    width = int(input("how is the width:"))
    gridTam = int(input("how grid space:"))

    scene = window(gridTam,title="Pathfind Test",width=width,height=height)
    scene.run() 