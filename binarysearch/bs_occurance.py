def binary_search(array, target):

    low = 0
    high = len(array) - 1

    while low < high:

        mid = low + (high - low) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:  # target is in the right side
            low = mid + 1
        else:  # target is in the right side
            mid = mid - 1

    return -1


array = [2, 3, 4, 10, 40]
target = 10

# Function call
result = binary_search(array, target)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")
