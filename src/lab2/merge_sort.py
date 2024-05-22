import math
import sys

def merge_sort(arr:list, start_index: int = 0, end_index: int | None = None):
    if end_index is None:
        end_index = len(arr) - 1
        
    if start_index < end_index:
        mid = math.floor((start_index + end_index) / 2.0)
        merge_sort(arr, start_index, mid)
        merge_sort(arr, mid + 1, end_index)
        merge(arr, start_index, mid, end_index)
    
    return arr
        

def merge(arr: list, start_index: int, mid: int, end_index: int):
    if start_index >= end_index: # cannot merge when there is only one element or the indices is malformed
        return arr

    size_1 = mid - start_index + 1
    size_2 = end_index - mid
    
    left_arr = []
    for i in range(size_1):
        left_arr.append(arr[start_index+i])
    left_arr.append(sys.maxsize)
    
    right_arr = []
    for j in range(size_2):
        right_arr.append(arr[mid + 1 + j])
    right_arr.append(sys.maxsize)
    
    i,j = 0,0
    for k in range(start_index, end_index + 1):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i = i + 1
        else:
            arr[k] = right_arr[j]
            j = j + 1
    return arr