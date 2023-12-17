def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    middle = len(nums)//2
    left_sorted, right_sorted = merge_sort(nums[:middle]), merge_sort(nums[middle:])
    sorted_nums = merge(left_sorted, right_sorted)
    return sorted_nums

def merge(left_sorted, right_sorted):
    sorted_nums = []
    while len(left_sorted) != 0:
        if len(right_sorted) == 0 or left_sorted[0] < right_sorted[0]:
            sorted_nums.append(left_sorted.pop(0))
        else:
            sorted_nums.append(right_sorted.pop(0))
    return sorted_nums + right_sorted