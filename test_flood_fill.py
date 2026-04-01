import unittest
from main import flood_fill

class TestFloodFill(unittest.TestCase):

    def test_basic_fill(self):
        grid = [
            ['W', 'W', 'W'],
            ['W', 'R', 'W'],
            ['W', 'W', 'W']
        ]
        start_r, start_c = 1, 1
        replacement = 'G'
        expected = [
            ['W', 'W', 'W'],
            ['W', 'G', 'W'],
            ['W', 'W', 'W']
        ]
        self.assertEqual(flood_fill(grid, start_r, start_c, replacement), expected)

    def test_area_fill(self):
        grid = [
            ['B', 'B', 'W'],
            ['B', 'W', 'W'],
            ['W', 'W', 'W']
        ]
        start_r, start_c = 0, 0
        replacement = 'G'
        expected = [
            ['G', 'G', 'W'],
            ['G', 'W', 'W'],
            ['W', 'W', 'W']
        ]
        self.assertEqual(flood_fill(grid, start_r, start_c, replacement), expected)

    def test_no_change_if_same_color(self):
        grid = [
            ['R', 'R'],
            ['R', 'R']
        ]
        start_r, start_c = 0, 0
        replacement = 'R'
        expected = [
            ['R', 'R'],
            ['R', 'R']
        ]
        self.assertEqual(flood_fill(grid, start_r, start_c, replacement), expected)

    def test_diagonal_isolation(self):
        grid = [
            ['R', 'W'],
            ['W', 'R']
        ]
        start_r, start_c = 0, 0
        replacement = 'G'
        expected = [
            ['G', 'W'],
            ['W', 'R']
        ]
        self.assertEqual(flood_fill(grid, start_r, start_c, replacement), expected)

    def test_complex_shape(self):
        grid = [
            ['X', 'X', 'X', 'Y'],
            ['X', 'Y', 'Y', 'Y'],
            ['X', 'X', 'X', 'Y']
        ]
        start_r, start_c = 0, 0
        replacement = 'C'
        expected = [
            ['C', 'C', 'C', 'Y'],
            ['C', 'Y', 'Y', 'Y'],
            ['C', 'C', 'C', 'Y']
        ]
        self.assertEqual(flood_fill(grid, start_r, start_c, replacement), expected)

if __name__ == '__main__':
    unittest.main()