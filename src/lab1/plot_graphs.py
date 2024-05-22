import random
import time

import matplotlib.pyplot as plt
import math
import numpy as np
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from merge_sort import merge_sort

from tqdm import tqdm
from pathlib import Path

LAB1_PATH = Path(__file__).parent
GRAPHS_FOLDER_PATH = LAB1_PATH.joinpath("graphs")


def get_n_random(n: int) -> list:
    """
    n: number of elements in the list

    Returns
    --------
    A list of length n containing random number between -1000 and 1000
    """

    return [random.randint(-1000, 1000) for _ in range(n)]

  
def plot_graphs(max_length: int = 2_000, step_size: int = 10, dpi_for_saved_image: float = 1000):
    """
    Plot graph for comparison of selection sort, various cases of insertion sort and merge sort.

    Parameters
    ----------
    max_length: The maximum length for list which is given for sorting algorithm
    step_size: Increment for choosing the next length of array
    dpi_for_saved_image: resolution in dots per inch for saved image
    """

    iteration_count = math.ceil(max_length / step_size)  # one greater to account for possible out of bounds error
    
    number = np.ndarray(shape=(iteration_count,))
    selection_diff_time = np.ndarray(shape=(iteration_count,))
    insertion_diff_time = np.ndarray(shape=(iteration_count,))
    insertion_best_diff_time = np.ndarray(shape=(iteration_count,))
    insertion_worst_diff_time = np.ndarray(shape=(iteration_count,))
    merge_sort_diff_time = np.ndarray(shape=(iteration_count,))

    for iteration_count, n_elements in enumerate(tqdm(range(1, max_length, step_size))):
        random_array = get_n_random(n_elements)
        
        selection_start = time.time()
        _ = selection_sort(random_array.copy())
        selection_end = time.time()
        
        insertion_start = time.time()
        insertion_sorted = insertion_sort(random_array.copy())
        insertion_end = time.time()

        insertion_best_start = time.time()
        insertion_sorted = insertion_sort(insertion_sorted.copy())
        insertion_best_end = time.time()

        merge_start = time.time()
        merge_sort(random_array) # no need to copy since it won't be used again
        merge_end = time.time()

        insertion_worst_start = time.time()
        _ = insertion_sort(insertion_sorted[::-1]) # no need to copy since it won't be used again
        insertion_worst_end = time.time()
        
        number[iteration_count] = n_elements
        selection_diff_time[iteration_count] = (selection_end - selection_start)
        insertion_diff_time[iteration_count] = (insertion_end - insertion_start)
        insertion_best_diff_time[iteration_count] = (insertion_best_end-insertion_best_start)
        insertion_worst_diff_time[iteration_count] = (insertion_worst_end-insertion_worst_start)
        merge_sort_diff_time[iteration_count] = (merge_end-merge_start)

    fig, ax = plt.subplots()
    ax.plot(number, selection_diff_time, label="Selection Sort")
    ax.plot(number, insertion_best_diff_time, label="Insertion Sort (Best Case)")
    ax.plot(number, insertion_diff_time, label="Insertion Sort")
    ax.plot(number, insertion_worst_diff_time, label="Insertion Sort (Worst Case)")
    ax.plot(number, merge_sort_diff_time, label="Merge Sort")

    ax.legend(loc = 'upper left')
    plt.xlabel("Number of Elements (n)")
    plt.ylabel("Time taken(t) [Seconds]")
    plt.savefig(GRAPHS_FOLDER_PATH.joinpath(f"graph_{max_length}.png"), format="png", dpi=dpi_for_saved_image)
    plt.show()
    

if __name__=="__main__":
    max_length_of_arrays = 2_000
    step_size = int(0.01 * max_length_of_arrays)

    plot_graphs(max_length_of_arrays, step_size)
