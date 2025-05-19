import time
from graphics import Cell

class Maze:
    def __init__(
            self, 
            x1, 
            y1, 
            num_rows, 
            num_cols, 
            cell_size_x, 
            cell_size_y, 
            win=None
        ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        for c in range(self.__num_cols):
            self.__cells.append([])
            for r in range(self.__num_rows):
                cell = Cell(self.__win)
                self.__cells[c].append(cell)
                self.__draw_cell(c, r)

    def __draw_cell(self, i, j):
        x1 = self.__x1 + (i * self.__cell_size_x)
        x2 = x1 + self.__cell_size_x
        y1 = self.__y1 + (j * self.__cell_size_y)
        y2 = y1 + self.__cell_size_y

        if self.__win is None:
            return
        
        self.__cells[i][j].draw(x1, x2, y1, y2)
        self.animate()

    def animate(self):
        if self.__win is None:
            return
        
        self.__win.redraw()
        time.sleep(0.04)

        
