import time
from graphics import *
from cell import Cell
import random

class Maze:
    def __init__(
            self, 
            x1, 
            y1, 
            num_rows, 
            num_cols, 
            cell_size_x, 
            cell_size_y, 
            win=None,
            seed=None
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
        self.__break_entrance_and_exit()
        if seed is not None:
            random.seed(seed)
        self.__break_walls_r(0, 0)

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
        time.sleep(0.02)

    def __break_entrance_and_exit(self):
        if len(self.__cells) == 0:
            return
        if len(self.__cells[0]) == 0:
            return 
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)

    def __break_walls_r(self, i, j):
        if self.__win is None:
            return
        
        self.__cells[i][j].visited = True
        
        while True:
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            moves = []

            for di, dj in directions:
                ni, nj = i + di, j + dj
                
                if 0 <= ni < self.__num_cols and 0 <= nj < self.__num_rows:
                    if not self.__cells[ni][nj].visited:
                        moves.append((ni, nj))
            
            if len(moves) == 0:
                self.__draw_cell(i, j)
                return
            
            random_index = random.randrange(0, len(moves))
            next_i, next_j = moves[random_index]

            di = next_i - i 
            dj = next_j - j

            if di == -1 and dj == 0:  # Moving up
                self.__cells[i][j].has_top_wall = False
                self.__cells[next_i][next_j].has_bottom_wall = False
            elif di == 0 and dj == 1:  # Moving right
                self.__cells[i][j].right = False
                self.__cells[next_i][next_j].has_left_wall = False
            elif di == 1 and dj == 0:  # Moving down
                self.__cells[i][j].bottom = False
                self.__cells[next_i][next_j].has_top_wall = False
            elif di == 0 and dj == -1:  # Moving left
                self.__cells[i][j].left = False
                self.__cells[next_i][next_j].has_right_wall = False

            self.__draw_cell(i, j)
            self.__draw_cell(next_i, next_j)

            self.__break_walls_r(next_i, next_j)
