import unittest
from bubble_sort import bubble_sort

class InsertionSortTest(unittest.TestCase):
    """Tests for insertion sort searching."""
    
    def test_sort_empty_list(self):
        self.assertEqual(bubble_sort([]), [])
    def test_sort_reversed_list(self):
        self.assertEqual(bubble_sort([5,4,3,2,1,0]), [0,1,2,3,4,5])
    def test_sort_sorted_list(self):
        self.assertEqual(bubble_sort([1,2,3,4]), [1,2,3,4])
    def test_sort_repeated_elements(self):
        self.assertEqual(bubble_sort([1,2,2,-3]), [-3,1,2,2])

if __name__ == "__main__":
    unittest.main()