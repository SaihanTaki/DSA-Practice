def insertion_sort(array):
    for i in range(1, len(array)):
        curr = array[i]
        for j in range(i):
            if curr < array[i - j - 1]:
                array[i - j] = array[i - j - 1]
                array[i - j - 1] = curr
    return array


# array = [8, 3, 2, 4, 1, 3, 2]
# print(insertion_sort(array))
