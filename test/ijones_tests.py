import unittest
import os
from ijones import execute_traversal


class TestIJones(unittest.TestCase):
    def run_logic_test(self, input_str, expected_output):
        with open("ijones.in", "w") as f:
            f.write(input_str)

        execute_traversal()

        with open("ijones.out", "r") as f:
            actual_output = f.read().strip()

        self.assertEqual(actual_output, str(expected_output))

    def test_standard_grid(self):
        self.run_logic_test("3 3\naaa\ncab\ndef", 5)

    def test_single_row(self):
        self.run_logic_test("10 1\nabcdefaghi", 2)

    def test_uniform_large_grid(self):
        grid_data = "7 6\n" + "aaaaaaa\n" * 6
        self.run_logic_test(grid_data.strip(), 201684)

    def tearDown(self):
        for filename in ["ijones.in", "ijones.out"]:
            if os.path.exists(filename):
                os.remove(filename)


if __name__ == "__main__":
    unittest.main()
