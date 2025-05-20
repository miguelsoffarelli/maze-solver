import unittest
from maze import Maze
from cell import Cell

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_one_cell(self):
        num_cols = 1
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_cell_size(self):
        cell_size_x = 100
        cell_size_y = 80
        m1 = Maze(0, 0, 4, 4, cell_size_x, cell_size_y)
        self.assertEqual(
            m1._Maze__cell_size_x,
            cell_size_x,
        )
        self.assertEqual(
            m1._Maze__cell_size_y,
            cell_size_y,
        )

    def test_maze_zero_cols(self):
        num_cols = 0
        num_rows = 0
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )

    def test_maze_zero_rows(self):
        num_cols = 1
        num_rows = 0
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_cell_isinstance_of_cell(self):
        m1 = Maze(0, 0, 5, 5, 10, 10)
        for col in range(len(m1._Maze__cells)):
            for row in range(len(m1._Maze__cells[col])):
                self.assertIsInstance(m1._Maze__cells[col][row], Cell)

    def test_entrance_and_exit(self):
        m1 = Maze(0, 0, 5, 5, 10, 10)
        m1._Maze__break_entrance_and_exit()
        self.assertEqual(
            m1._Maze__cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._Maze__cells[m1._Maze__num_cols - 1][m1._Maze__num_rows - 1].has_bottom_wall,
            False,
        )

if __name__ == "__main__":
    unittest.main()