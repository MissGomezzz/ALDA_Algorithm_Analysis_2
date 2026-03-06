#Note: tests generated with ChatGPT

import unittest

from src.searching import (
    linear_search,
    binary_search,
    jump_search,
    interpolation_search,
    exponential_search
)


class TestSearchingAlgorithms(unittest.TestCase):

    def setUp(self):
        self.sorted_array = [1, 3, 5, 7, 9, 11, 13]
        self.unsorted_array = [9, 1, 13, 3, 7, 11, 5]


    # -----------------------------
    # LINEAR SEARCH TESTS
    # -----------------------------

    def test_linear_search_found(self):
        result = linear_search(self.unsorted_array, 7)
        self.assertNotEqual(result, -1)
        self.assertEqual(self.unsorted_array[result], 7)

    def test_linear_search_not_found(self):
        result = linear_search(self.unsorted_array, 100)
        self.assertEqual(result, -1)


    # -----------------------------
    # BINARY SEARCH TESTS
    # -----------------------------

    def test_binary_search_found(self):
        result = binary_search(self.sorted_array, 9)
        self.assertEqual(result, 4)

    def test_binary_search_not_found(self):
        result = binary_search(self.sorted_array, 100)
        self.assertEqual(result, -1)


    # -----------------------------
    # JUMP SEARCH TESTS
    # -----------------------------

    def test_jump_search_found(self):
        result = jump_search(self.sorted_array, 11)
        self.assertEqual(result, 5)

    def test_jump_search_not_found(self):
        result = jump_search(self.sorted_array, 50)
        self.assertEqual(result, -1)


    # -----------------------------
    # INTERPOLATION SEARCH TESTS
    # -----------------------------

    def test_interpolation_search_found(self):
        result = interpolation_search(self.sorted_array, 5)
        self.assertEqual(result, 2)

    def test_interpolation_search_not_found(self):
        result = interpolation_search(self.sorted_array, 42)
        self.assertEqual(result, -1)


    # -----------------------------
    # EXPONENTIAL SEARCH TESTS
    # -----------------------------

    def test_exponential_search_found(self):
        result = exponential_search(self.sorted_array, 13)
        self.assertEqual(result, 6)

    def test_exponential_search_not_found(self):
        result = exponential_search(self.sorted_array, -5)
        self.assertEqual(result, -1)


if __name__ == "__main__":
    unittest.main()