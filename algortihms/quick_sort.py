"""
Quick Sort Algorithm:
- Selects a pivot and partitions the array into elements smaller and greater than the pivot.
- Time Complexity: O(n log n) on average, O(n^2) in worst case (bad pivot selection).
"""
def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
