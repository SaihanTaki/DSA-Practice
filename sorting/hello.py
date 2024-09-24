#!/usr/bin/python

import copy

li1 = [1, 2, [3, 5], 4]
print("li1 ID: ", id(li1), "Value: ", li1)


li2 = copy.copy(li1)
print("li2 ID: ", id(li2), "Value: ", li2)
li3 = copy.deepcopy(li1)
print("li3 ID: ", id(li3), "Value: ", li3)
li4 = li1
print("li4 ID: ", id(li4), "Value: ", li4)

li1[0] = "y"

li4[2][0] = "x"
print("li1 ID: ", id(li1), "Value: ", li1)
print("li4 ID: ", id(li4), "Value: ", li4)


li2[2][0] = "shallow copy"
print("li1 ID: ", id(li1), "Value: ", li1)
print("li2 ID: ", id(li2), "Value: ", li2)


li3[2][0] = "deep copy"
print("li1 ID: ", id(li1), "Value: ", li1)
print("li3 ID: ", id(li3), "Value: ", li3)


def myfunc_1(arr):
    arr.pop()
    return arr


def myfunc_2(arr):
    return arr


array = [1, 2, 3]
print(f"First function returns = {myfunc_1(array)}")
print(f"Second function returns = {myfunc_2(array)}")


def myfunc(**args):
    a = args["d"]
    return a


print(myfunc(a=1, d=2, c=3))
print(__name__)
