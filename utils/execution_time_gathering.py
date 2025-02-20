import time
import pandas as pd
from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort
from data_generator.generator import get_random_list

def measure_execution_time(algorithm, data):
    """
    Measures the execution time of a sorting algorithm.

    :param algorithm: Sorting function.
    :param data: List to be sorted.
    :return: Execution time in seconds.
    """
    start_time = time.time()
    algorithm(data.copy())
    return time.time() - start_time

def gather_execution_times(min_size, max_size, step, samples_per_size):
    """
    Collects execution times for different input sizes.

    :param min_size: Minimum list size.
    :param max_size: Maximum list size.
    :param step: Step size for increasing list size.
    :param samples_per_size: Number of samples per size.
    :return: Pandas DataFrame with execution times.
    """
    results = []

    for size in range(min_size, max_size + 1, step):
        for _ in range(samples_per_size):
            data = get_random_list(size)
            results.append({
                'Size': size,
                'BubbleSort': measure_execution_time(bubble_sort, data),
                'InsertionSort': measure_execution_time(insertion_sort, data),
                'MergeSort': measure_execution_time(merge_sort, data),
                'QuickSort': measure_execution_time(quick_sort, data)
            })

    return pd.DataFrame(results).groupby("Size", as_index=False).mean()
