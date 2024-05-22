def generate_array_for_quick_sort_best_case(
    arr, start_index: int = 0, end_index: int | None = None
) -> list[int]:
    """
    For best case of the quick sort, for each recursive call, pivot is the median
    """

    if end_index is None:
        end_index = len(arr) - 1

    if start_index > end_index:
        return []

    if (start_index == 0) and (end_index == (len(arr) - 1)):  # only sorting once
        arr = sorted(arr)

    median = int((start_index + end_index) // 2)

    i = median
    # move the median to last index
    while i < end_index:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        i += 1

    _ = generate_array_for_quick_sort_best_case(arr, start_index, median - 1)
    _ = generate_array_for_quick_sort_best_case(arr, median, end_index - 1)

    return arr  # this return is only useful for the non-recursive calling function, all other arrays are same


def generate_array_for_merge_sort_worst_case(arr: list, sort=True):
    """
    For the worst case of merge sort, the left and right sub-array involved
    in merge operation should store alternate elements of the sorted array.
    """

    n = len(arr)

    if n <= 1:
        return arr

    if sort:
        sorted_array = sorted(arr)
    else:
        sorted_array = arr.copy()

    if n == 2:
        sorted_array[0], sorted_array[1] = sorted_array[1], sorted_array[0]
        return sorted_array

    left_arr = sorted_array[::2]  # take elements at even indices
    right_arr = sorted_array[1::2]  # take elements at odd indices

    return generate_array_for_merge_sort_worst_case(
        left_arr, sort=False
    ) + generate_array_for_merge_sort_worst_case(right_arr, sort=False)
