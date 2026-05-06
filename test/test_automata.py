import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from automata_search import search_finite_automata


class TestFiniteAutomataSearch(unittest.TestCase):

    def test_multiple_occurrences(self):
        text = "АБАБАКАНАБАБА"
        pattern = "АБА"
        self.assertEqual(search_finite_automata(text, pattern), [0, 2, 8, 10])

    def test_no_match(self):
        self.assertEqual(search_finite_automata("abcdef", "xyz"), [])

    def test_empty_needle(self):
        self.assertEqual(search_finite_automata("abc", ""), [])

    def test_empty_haystack(self):
        self.assertEqual(search_finite_automata("", "а"), [])

    def test_overlapping_chars(self):
        self.assertEqual(search_finite_automata("aaaaa", "aa"), [0, 1, 2, 3])

    def test_needle_longer_than_haystack(self):
        self.assertEqual(search_finite_automata("python", "python_is_cool"), [])

    def test_case_sensitivity(self):
        self.assertEqual(search_finite_automata("Київ", "київ"), [])

    def test_single_character(self):
        self.assertEqual(search_finite_automata("mississippi", "i"), [1, 4, 7, 10])

    def test_complex_pattern(self):
        self.assertEqual(search_finite_automata("ababcababcabc", "ababc"), [0, 5])


if __name__ == "__main__":
    unittest.main()
