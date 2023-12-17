def selection_sort(arr):
    for i in range(len(arr) - 1):
        selected_num_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[selected_num_index]:
                selected_num_index = j
        arr[i], arr[selected_num_index] = arr[selected_num_index], arr[i]