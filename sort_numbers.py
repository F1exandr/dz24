def sort_numbers(numbers):
    return sorted(numbers)

# test_sort_numbers.py

import unittest
from sort_numbers import sort_numbers

class TestSortNumbers(unittest.TestCase):
    def test_sort_numbers(self):
        self.assertEqual(sort_numbers([5, 2, 8, 1, 3]), [1, 2, 3, 5, 8])
        self.assertEqual(sort_numbers([10, 5, 8]), [5, 8, 10])
        self.assertEqual(sort_numbers([-2, -5, 0, 3]), [-5, -2, 0, 3])

if __name__ == "__main__":
    unittest.main()