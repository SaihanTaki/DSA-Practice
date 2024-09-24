def binary_search(low, high, func):

    while low < high:
        mid = (high + low) // 2

        if func(mid) > 0:
            high = mid - 1
        elif func(mid) < 0:
            low = mid + 1
        else:
            return mid
    return -1


def isCorrect(n):
    target = 10
    if n > target:
        return 1
    elif n < target:
        return -1
    else:
        return 0


print(binary_search(1, 30, isCorrect))
