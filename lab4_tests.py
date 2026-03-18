import unittest
from avl_priority_queue import AVLPriorityQueue


class TestAVLPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.queue = AVLPriorityQueue()

    def test_insert_and_peek(self):
        self.queue.insert("A", 1)
        self.queue.insert("B", 5)
        self.queue.insert("C", 3)

        self.assertEqual(self.queue.peek(), ("B", 5))

    def test_pop(self):
        self.queue.insert("A", 1)
        self.queue.insert("B", 5)

        self.assertEqual(self.queue.pop(), ("B", 5))
        self.assertEqual(self.queue.pop(), ("A", 1))

    def test_empty_queue(self):
        self.assertIsNone(self.queue.peek())
        self.assertIsNone(self.queue.pop())

    def test_same_priority(self):
        self.queue.insert("A", 2)
        self.queue.insert("B", 2)

        first = self.queue.pop()
        second = self.queue.pop()

        self.assertEqual(first[1], 2)
        self.assertEqual(second[1], 2)

    def test_single_element(self):
        self.queue.insert("X", 10)
        self.assertEqual(self.queue.peek(), ("X", 10))
        self.assertEqual(self.queue.pop(), ("X", 10))
        self.assertIsNone(self.queue.peek())


if __name__ == "__main__":
    unittest.main()