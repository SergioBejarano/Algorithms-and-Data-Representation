"""
Bubble Sort Algorithm:
- Repeatedly swaps adjacent elements if they are in the wrong order.
- Time Complexity: O(n^2) in worst and average cases, O(n) in best case (already sorted array).
"""
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
