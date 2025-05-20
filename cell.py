from graphics import *

class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window
        self.visited = False

    def draw(self, x1, x2, y1, y2):
        if self.__win is None:
            return
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        
        if self.has_left_wall:
            p1 = Point(self.__x1, self.__y1)
            p2 = Point(self.__x1, self.__y2)
            l = Line(p1, p2)
            self.__win.draw_line(l, "black")
        else:
            p1 = Point(self.__x1, self.__y1)
            p2 = Point(self.__x1, self.__y2)
            l = Line(p1, p2)
            self.__win.draw_line(l, "white")

        if self.has_top_wall:
            p1 = Point(self.__x1, self.__y1)
            p2 = Point(self.__x2, self.__y1)
            l = Line(p1, p2)
            self.__win.draw_line(l, "black")
        else:
            p1 = Point(self.__x1, self.__y1)
            p2 = Point(self.__x2, self.__y1)
            l = Line(p1, p2)
            self.__win.draw_line(l, "white")

        if self.has_right_wall:
            p1 = Point(self.__x2, self.__y1)
            p2 = Point(self.__x2, self.__y2)
            l = Line(p1, p2)
            self.__win.draw_line(l, "black")
        else:
            p1 = Point(self.__x2, self.__y1)
            p2 = Point(self.__x2, self.__y2)
            l = Line(p1, p2)
            self.__win.draw_line(l, "white")

        if self.has_bottom_wall:
            p1 = Point(self.__x1, self.__y2)
            p2 = Point(self.__x2, self.__y2)
            l = Line(p1, p2)
            self.__win.draw_line(l, "black")
        else:
            p1 = Point(self.__x1, self.__y2)
            p2 = Point(self.__x2, self.__y2)
            l = Line(p1, p2)
            self.__win.draw_line(l, "white")

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"

        from_x = (self.__x1 + self.__x2) / 2
        from_y = (self.__y1 + self.__y2) / 2
        to_x = (to_cell.__x1 + to_cell.__x2) / 2
        to_y = (to_cell.__y1 + to_cell.__y2) / 2

        p1 = Point(from_x, from_y)
        p2 = Point(to_x, to_y)
        l = Line(p1, p2)
        
        self.__win.draw_line(l, color)