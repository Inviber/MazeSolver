import unittest
from main import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_create_large(self):
        num_cols = 24
        num_rows = 20
        m2 = Maze(0, 0, num_rows, num_cols, 15, 15)
        self.assertEqual(len(m2._cells), num_cols)
        self.assertEqual(len(m2._cells[0]), num_rows)
    
    def test_maze_break(self):
        num_cols = 12
        num_rows = 10
        m3 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(m3._cells[0][0].has_top_wall, False)
        self.assertEqual(m3._cells[num_cols-1][num_rows-1].has_bottom_wall, False)

    def test_maze_cell_reset(self):
        num_cols = 12
        num_rows = 10
        m4 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(m4._cells[0][0].visited, False)
        self.assertEqual(m4._cells[num_cols-1][num_rows-1].visited, False)

if __name__ == "__main__":
    unittest.main()