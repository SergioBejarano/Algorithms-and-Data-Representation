"""
Insertion Sort Algorithm:
- Builds the sorted array one element at a time by shifting elements.
- Time Complexity: O(n^2) in worst and average cases, O(n) in best case.
"""
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

