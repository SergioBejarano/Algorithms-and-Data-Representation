"""
Merge Sort Algorithm:
- Recursively divides the array into halves and merges sorted halves.
- Time Complexity: O(n log n) in all cases.
"""
def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = merge_sort(array[:mid])
        right_half = merge_sort(array[mid:])

        merged = []
        i = j = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                merged.append(left_half[i])
                i += 1
            else:
                merged.append(right_half[j])
                j += 1
        merged.extend(left_half[i:])
        merged.extend(right_half[j:])
        return merged
    else:
        return array
