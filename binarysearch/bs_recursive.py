def binary_search(array, target, low=None, high=None):

    low = low if low else 0
    high = high if high else len(array) - 1
    mid = low + (high - low) // 2

    if low <= high:
        if target == array[mid]:
            return mid
        elif target > array[mid]:
            return binary_search(array, target, mid + 1, high)
        else:
            return binary_search(array, target, low, mid - 1)

    return -1


array = [2, 3, 4, 10, 40]
target = 40

# Function call
result = binary_search(array, target)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")
