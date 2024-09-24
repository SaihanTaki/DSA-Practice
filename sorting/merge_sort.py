def merge_sort(array):
    if len(array) <= 1:
        return array

    half = len(array) // 2
    left = array[:half]
    right = array[half:]
    sarray = []

    left = merge_sort(left)
    right = merge_sort(right)

    while left and right:
        if left[0] <= right[0]:
            sarray.append(left.pop(0))
        else:
            sarray.append(right.pop(0))
    if left:
        sarray.extend(left)
    if right:
        sarray.extend(right)

    return sarray


# array = [8, 3, 2, 4, 1, 3, 2]
# print(merge_sort(array))
