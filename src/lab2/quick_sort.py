import sys

NEW_RECURSION_LIMIT = 5000
print(
    f" Increasing the recursion limit from {sys.getrecursionlimit()} to {NEW_RECURSION_LIMIT}"
)
sys.setrecursionlimit(NEW_RECURSION_LIMIT)


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr, p: int = 0, r: int | None = None):
    if r is None:
        r = len(arr) - 1

    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q - 1)
        quick_sort(arr, q + 1, r)

    return arr


def partition(arr, p, r) -> int:
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            swap(arr, i, j)
    swap(arr, i + 1, r)
    return i + 1
