from typing import List


def countStudents(students: List[int], sandwiches: List[int]) -> int:
    while sandwiches:
        if students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)
        elif students[0] != sandwiches[0]:
            students.append(students.pop(0))
    return len(students)


students = [1, 1, 1, 0, 0, 1]
sandwiches = [1, 0, 0, 0, 1, 1]

print(countStudents(students, sandwiches))
