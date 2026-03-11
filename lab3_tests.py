import unittest
from binary_tree import BinaryTree, find_successor

class TestFindSuccessor(unittest.TestCase):
    def setUp(self):
        self.root = BinaryTree(10)
        
        self.node_5 = BinaryTree(5, parent=self.root)
        self.node_15 = BinaryTree(15, parent=self.root)
        self.root.left = self.node_5
        self.root.right = self.node_15

        self.node_3 = BinaryTree(3, parent=self.node_5)
        self.node_7 = BinaryTree(7, parent=self.node_5)
        self.node_5.left = self.node_3
        self.node_5.right = self.node_7

        self.node_12 = BinaryTree(12, parent=self.node_7)
        self.node_7.left = self.node_12

        self.node_20 = BinaryTree(20, parent=self.node_15)
        self.node_15.right = self.node_20

    def test_successor_7_is_10(self):
        result = find_successor(self.root, self.node_7)
        self.assertEqual(result.value, 10)

    def test_successor_12_is_7(self):
        result = find_successor(self.root, self.node_12)
        self.assertEqual(result.value, 7)

    def test_successor_5_is_12(self):
        result = find_successor(self.root, self.node_5)
        self.assertEqual(result.value, 12)

    def test_successor_root_10_is_15(self):
        result = find_successor(self.root, self.root)
        self.assertEqual(result.value, 15)

    def test_successor_last_node_is_none(self):
        result = find_successor(self.root, self.node_20)
        self.assertIsNone(result)

    def test_none_input(self):
        result = find_successor(self.root, None)
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()