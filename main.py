from graphics import *

def main():
    win = Window(800, 600)
    
    c1 = Cell(win)
    c1.draw(100, 200, 100, 200)
    c2 = Cell(win)
    c2.draw(100, 200, 300, 400)
    c3 = Cell(win)
    c3.draw(100, 400, 600, 800)
    c4 = Cell(win)
    c4.draw(450, 600, 10, 250)

    c1.has_bottom_wall = False
    c1.has_top_wall = False
    c1.has_right_wall = False
    c1.draw_move(c2)
    
    c2.draw_move(c3, True)
    c2.draw_move(c4)
    
    c3.has_left_wall = False
    c3.draw_move(c1)
    
    c4.has_left_wall, c4.has_right_wall = False, False
    c4.draw_move(c3, True)

    win.wait_for_close()

main()

