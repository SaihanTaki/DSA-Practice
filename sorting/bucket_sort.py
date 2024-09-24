import math


def bucket_sort(array):
    if len(array) <= 1:
        return array

    n = max(array) + 1
    diff = math.ceil((max(array) - min(array)) / n)
    bucket = []

    for i in range(n):
        bucket.append([])

    for item in array:
        index = item // diff
        bucket[index].append(item)

    for i in range(n):
        bucket[i] = sorted(bucket[i])

    k = 0
    for i in range(n):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array


# array = [8, 9, 3, 2, 4, 1, 3, 2]
# array = [2, 1, 0]
# print(f"Bucket Sort:    {bucket_sort(array)}")
