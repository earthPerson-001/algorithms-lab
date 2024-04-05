import random
import time

import matplotlib.pyplot as plt
from insertion_sort import insertion_sort
from selection_sort import selection_sort

from tqdm import tqdm


def get_n_random(n: int) -> list:
    """"
    n: number of elements in the list

    Returns
    --------
    A list of length n containing random number between -1000 and 1000
    """

    return [random.randint(-1000, 1000) for _ in range(n)]

  
def plot_graphs():
    max_length = 50_000
    step_size = 1000
    
    number = []
    selection_diff_time = []
    insertion_diff_time = []
    insertion_best_diff_time = []
    insertion_worst_diff_time = []

    for i in tqdm(range(10, max_length, step_size)):
        random_array = get_n_random(i)
        
        selection_start = time.time()
        _ = selection_sort(random_array.copy())
        selection_end = time.time()
        
        insertion_start = time.time()
        insertion_sorted = insertion_sort(random_array.copy())
        insertion_end = time.time()

        insertion_best_start = time.time()
        insertion_sorted = insertion_sort(insertion_sorted.copy())
        insertion_best_end = time.time()

        insertion_worst_start = time.time()
        insertion_sorted = insertion_sort(insertion_sorted.copy()[::-1])
        insertion_worst_end = time.time()
        
        number.append(i)
        selection_diff_time.append(selection_end - selection_start)
        insertion_diff_time.append(insertion_end - insertion_start)
        insertion_best_diff_time.append(insertion_best_end-insertion_best_start)
        insertion_worst_diff_time.append(insertion_worst_end-insertion_worst_start)

    fig, ax = plt.subplots()
    ax.plot(number, selection_diff_time, label="Selection Sort")
    ax.plot(number, insertion_best_diff_time, label="Insertion Sort (Best Case)")
    ax.plot(number, insertion_diff_time, label="Insertion Sort")
    ax.plot(number, insertion_worst_diff_time, label="Insertion Sort (Worst Case)")
    ax.legend(loc = 'upper left')
    plt.xlabel("Number of Elements (n)")
    plt.ylabel("Time taken(t) [Seconds]")
    plt.show()
    

if __name__=="__main__":
    plot_graphs()
