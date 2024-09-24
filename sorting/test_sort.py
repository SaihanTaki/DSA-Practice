from merge_sort import merge_sort
from insertion_sort import insertion_sort
from quick_sort import quick_sort
from bucket_sort import bucket_sort


array = [8, 3, 2, 4, 1, 0, -2, 3, 2, 0.79, 1.2]
# array = [2, 0, 1]

print(f"Unsorted Array: {array}")
print()
print(f"Insertion Sort: {insertion_sort(array)}")
print(f"Merge Sort:     {merge_sort(array)}")
print(f"Quick Sort:     {quick_sort(array)}")
# print(f"Bucket Sort:    {bucket_sort(array)}")
