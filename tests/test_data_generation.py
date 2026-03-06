#Note: tests generated with ChatGPT

import unittest

from src.data_generator import (
    generate_sorted_data,
    generate_target
)


class TestDataGenerator(unittest.TestCase):

    def test_sorted_data_size(self):
        size = 50
        arr = generate_sorted_data(size)

        self.assertEqual(len(arr), size)

    def test_sorted_data_is_sorted(self):
        size = 50
        arr = generate_sorted_data(size)

        self.assertEqual(arr, sorted(arr))

    def test_generate_target_exists_in_data(self):
        size = 100
        arr = generate_sorted_data(size)
        target = generate_target(arr)

        self.assertIn(target, arr)


if __name__ == "__main__":
    unittest.main()