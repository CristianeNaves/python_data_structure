"""https://www.youtube.com/watch?v=wx5juM9bbFo&t=1021s"""

def quick_sort(arr, begin=0, end=None):
    if end is None:
        end = len(arr) - 1
    
    if begin < end:
        p = partition(arr, begin, end)
        quick_sort(arr, begin, p-1)
        quick_sort(arr, p+1, end)

def partition(arr, begin, end):
    pivot = arr[end]
    i = begin

    for j in range(begin, end):
        if arr[j] <= pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i = i + 1
    arr[end], arr[i] = arr[i], arr[end]
    return i
