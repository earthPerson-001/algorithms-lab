"""
Selection Sort implementation
"""


def selection_sort(arr: list) -> list:

    n = len(arr)

    for i in range(n):
        smallest = i
        for j in range(i+1, n):
            if arr[j] < arr[smallest]:
                smallest = j

        arr[smallest], arr[i] = arr[i], arr[smallest]
            
    return arr
