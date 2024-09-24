from linked_list import LinkedList, ListNode, print_linked_list
import unittest


# Creating a linked list using LinkedList helper class
mylist = LinkedList()
mylist.fromArray([1, 2, 3, 4])
print(len(mylist))
mylist.printList()
mylist.removeByIndex(3)

mylist.printList()

mylist.insertEnd(7)

mylist.printList()
print_linked_list(mylist.head)


# Creating a linked list using ListNode
head = ListNode(3)
head.next = ListNode(5)
head.next.next = ListNode(7)
print_linked_list(head)


# testing using a single length linked list
mylist = LinkedList()
mylist.insertEnd(9)
print(mylist.__len__())
mylist.printList()
print_linked_list(mylist.head)

head = ListNode(3)
print_linked_list(head)

# tesing using a empty linked list
print(len(LinkedList()))
print_linked_list(ListNode())
print_linked_list(LinkedList().head)
LinkedList().printList()


mylist = LinkedList()
mylist.fromArray([6, 1, 2, 6, 3, 6, 4, 6])
# mylist.fromArray([1, 6, 6, 1])
print(len(mylist))
mylist.printList()
mylist.removeByValue(6)
mylist.printList()


mylist = LinkedList()
mylist.fromArray([1, 2, 4])
mylist.printList()
mylist.insertAtIndex(3, 4)
print(mylist.tail)
mylist.printList()


class TestLinkedList(unittest.TestCase):
    def test_removeByIndex():
        pass
