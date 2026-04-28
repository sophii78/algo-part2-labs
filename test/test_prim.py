import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from main import prim_mst


class TestPrimAlgorithm(unittest.TestCase):

    def test_simple_graph(self):
        matrix = [[0, 10, 20], [10, 0, 15], [20, 15, 0]]
        self.assertEqual(prim_mst(matrix, 3), 25.0)

    def test_disconnected_graph(self):
        matrix = [[0, 5, 0], [5, 0, 0], [0, 0, 0]]
        self.assertEqual(prim_mst(matrix, 3), 5.0)

    def test_single_node(self):
        matrix = [[0]]
        self.assertEqual(prim_mst(matrix, 1), 0)


if __name__ == "__main__":
    unittest.main()
