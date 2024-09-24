def quick_sort(array):
    if len(array) <= 1:
        return array

    left, right = [], []

    pivot = array[-1]
    length = len(array) - 1

    for i in range(length):
        if array[i] <= pivot:
            left.append(array[i])
        else:
            right.append(array[i])

    return quick_sort(left) + [pivot] + quick_sort(right)


# array = [8, 3, 2, 4, 1, 3, 2]
# print(quick_sort(array))
