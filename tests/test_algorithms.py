import unittest
from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort

class TestSortingAlgorithms(unittest.TestCase):

    def setUp(self):
        """Initialize various test cases."""
        self.unsorted_list = [64, 34, 25, 12, 22, 11, 90]
        self.sorted_list = [11, 12, 22, 25, 34, 64, 90]

        self.empty_list = []
        self.single_element_list = [42]
        self.duplicate_list = [5, 3, 8, 3, 5, 9, 3, 2, 5]
        self.sorted_duplicate_list = [2, 3, 3, 3, 5, 5, 5, 8, 9]

        self.already_sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.reverse_sorted_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

        self.large_list = list(range(1000, 0, -1))
        self.large_sorted_list = list(range(1, 1001))

    def run_sort_test(self, sorting_function):
        """Helper method to test sorting function with various cases."""
        self.assertEqual(sorting_function(self.unsorted_list.copy()), self.sorted_list)
        self.assertEqual(sorting_function(self.empty_list.copy()), [])
        self.assertEqual(sorting_function(self.single_element_list.copy()), [42])
        self.assertEqual(sorting_function(self.duplicate_list.copy()), self.sorted_duplicate_list)
        self.assertEqual(sorting_function(self.already_sorted_list.copy()), self.already_sorted_list)
        self.assertEqual(sorting_function(self.reverse_sorted_list.copy()), self.already_sorted_list)
        self.assertEqual(sorting_function(self.large_list.copy()), self.large_sorted_list)

    def test_bubble_sort(self):
        """Test bubble sort algorithm."""
        self.run_sort_test(bubble_sort)

    def test_insertion_sort(self):
        """Test insertion sort algorithm."""
        self.run_sort_test(insertion_sort)

    def test_merge_sort(self):
        """Test merge sort algorithm."""
        self.run_sort_test(merge_sort)

    def test_quick_sort(self):
        """Test quick sort algorithm."""
        self.run_sort_test(quick_sort)

if __name__ == '__main__':
    unittest.main()
