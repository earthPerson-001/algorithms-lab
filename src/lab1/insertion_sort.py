"""
Insertion sort implementation
"""

def insertion_sort(arr:list) -> list:

    for i in range(1, len(arr)):
        j = i
        swap_with = arr[i]
        while( j > 0 and arr[j-1] > swap_with):
            arr[j] = arr[j-1]
            j -= 1
        
        arr[j] = swap_with
        
    return arr


if __name__=="__main__":
    arr = [2,0,3,1,5]
    return_arr = insertion_sort(arr)

    print("After applying insertion sort: ", return_arr)
