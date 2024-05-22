import random
import time
import matplotlib.pyplot as plt

from pathlib import Path
import sys
import math

PROJECT_PATH = Path(__file__).parents[1]
if PROJECT_PATH.absolute().__str__() not in sys.path:
    sys.path.append(PROJECT_PATH.absolute().__str__())

from lab1.insertion_sort import insertion_sort
from lab1.selection_sort import selection_sort

from lab2.merge_sort import merge_sort
from lab2.quick_sort import quick_sort

from lab2.generate_array_for_various_cases import generate_array_for_merge_sort_worst_case, generate_array_for_quick_sort_best_case


def get_n_random(n: int):

    return [random.randint(-1000, 10000) for _ in range(n)]


def main():
    max_length = 5000
    number = []
    selection_diff_time = []
    insertion_diff_time = []
    merge_diff_time = []
    quick_sort_diff_time = []
    merge_best_diff_time = []
    merge_worst_diff_time = []
    quick_sort_best_diff_time = []
    quick_sort_worst_diff_time = []
    for i in range(10, max_length, int(0.1 * max_length)):
        random_array = get_n_random(i)

        selection_start = time.time_ns()
        sorted_array = selection_sort(
            random_array.copy()
        ).copy()  # keeping a copy for later use
        selection_end = time.time_ns()

        insertion_start = time.time_ns()
        _ = insertion_sort(random_array.copy())
        insertion_end = time.time_ns()

        merge_start = time.time_ns()
        _ = merge_sort(random_array.copy())
        merge_end = time.time_ns()

        # TODO: Vefity the implementation method to generate array for best case of merge sort
        copy_arr = sorted_array.copy()
        merge_start_best = time.time_ns()
        _ = merge_sort(copy_arr)
        merge_end_best = time.time_ns()

        # For worst case of merge sort, the left and right  sub-array involved
        # in merge operation should store alternate elements of sorted array.
        array_for_worst_merge_sort = generate_array_for_merge_sort_worst_case(sorted_array, sort=False)

        merge_start_worst = time.time_ns()
        _ = merge_sort(array_for_worst_merge_sort)
        merge_end_worst = time.time_ns()

        quick_sort_start = time.time_ns()
        _ = quick_sort(random_array)
        quick_sort_end = time.time_ns()

        copy_arr = sorted_array.copy()
        quick_sort_start_worst = time.time_ns()
        _ = quick_sort(copy_arr)  # run on the sorted array
        quick_sort_end_worst = time.time_ns()

        quick_best_arr = generate_array_for_quick_sort_best_case(random_array.copy())
        quick_sort_start_best = time.time_ns()
        _ = quick_sort(quick_best_arr) 
        quick_sort_end_best = time.time_ns()

        number.append(i)
        selection_diff_time.append(1e-6 * (selection_end - selection_start))
        insertion_diff_time.append(1e-6 * (insertion_end - insertion_start))
        merge_diff_time.append(1e-6 * (merge_end - merge_start))
        quick_sort_diff_time.append(1e-6 * (quick_sort_end - quick_sort_start))
        quick_sort_worst_diff_time.append(
            1e-6 * (quick_sort_end_worst - quick_sort_start_worst)
        )
        quick_sort_best_diff_time.append(
            1e-6 * (quick_sort_end_best - quick_sort_start_best)
        )
        merge_worst_diff_time.append(1e-6 * (merge_end_worst - merge_start_worst))
        merge_best_diff_time.append(1e-6 * (merge_end_best - merge_start_best))

    fig, axs = plt.subplots(2, 2)
    axs[0, 0].plot(number, selection_diff_time, label="Selection Sort", color="r")
    axs[0, 0].plot(number, insertion_diff_time, label="Insertion Sort", color="g")

    axs[0, 1].plot(number, quick_sort_diff_time, label="Quick Sort")
    axs[0, 1].plot(number, merge_diff_time, label="Merge Sort")

    axs[1, 0].plot(number, quick_sort_worst_diff_time, label="Quick Sort(Worst)")
    axs[1, 0].plot(number, merge_worst_diff_time, label="Merge Sort(Worst)")

    axs[1, 1].plot(number, quick_sort_best_diff_time, label="Quick Sort(Best)")
    axs[1, 1].plot(number, merge_best_diff_time, label="Merge Sort(Best)")

    for ax in axs.flat:
        ax.grid(True)
        ax.legend(loc="upper left")
        ax.set(xlabel="Number [N]", ylabel="Time [ms]")

    plt.show()


if __name__ == "__main__":
    main()
