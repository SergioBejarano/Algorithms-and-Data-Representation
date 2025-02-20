import pandas as pd
import matplotlib.pyplot as plt
from utils.execution_time_gathering import gather_execution_times

def plot_execution_times(df):
    """
    Plots execution times of sorting algorithms.

    :param df: DataFrame with execution times.
    """
    plt.figure(figsize=(12, 8))

    for algorithm in ['BubbleSort', 'InsertionSort', 'MergeSort', 'QuickSort']:
        if algorithm in df.columns:
            plt.plot(df['Size'], df[algorithm], label=algorithm)

    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Sorting Algorithms Execution Time Analysis')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    # Parameters
    min_size = 100
    max_size = 1000
    step = 100
    samples_per_size = 5

    # Gather execution times
    df = gather_execution_times(min_size, max_size, step, samples_per_size)

    # Plot execution times
    plot_execution_times(df)

if __name__ == '__main__':
    main()
