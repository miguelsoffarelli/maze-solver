from graphics import *
from maze import *

def main():
    win = Window(800, 600)
    
    maze = Maze(10, 10, 10, 10, 50, 50, win, True)
    maze.solve()

    win.wait_for_close()

main()

