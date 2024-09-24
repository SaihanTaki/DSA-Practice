from linked_list import LinkedList, ListNode, print_linked_list
from typing import Optional


def reverse_iterative(head: Optional[ListNode] = None):
    if not head:
        return head
    # check if head is a dummy node or not \\
    # if head is a dummy node (linked list is defined using LinkedList \\
    # helper class) then the actual head or first element of the linked \\
    # list should be head.next
    # if head.val is None:
    #     current_node = head.next
    # else:
    #     current_node = head

    current_node = head
    prev_node = None
    while current_node:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
    return prev_node


def reverse_recursive(head: ListNode):
    # if head is None --> this base condition is for if \\
    # the functions get an empty list
    # if head.next is None --> this base condition is for \\
    # to get the last element
    if not head or not head.next:
        return head
    reversed_list_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return reversed_list_head


# Creating a linked list using LinkedList helper class
mylist = LinkedList()
mylist.fromArray([1, 2, 3, 4])
mylist.printList()
head = reverse_iterative(mylist.head)
print_linked_list(head)


# Creating a linked list using ListNode
head = ListNode(3)
head.next = ListNode(5)
head.next.next = ListNode(7)
head.next.next.next = ListNode(9)
print_linked_list(head)
head = reverse_iterative(head)
print_linked_list(head)


# test using a single length linked list
mylist = LinkedList()
mylist.fromArray([7])
mylist.printList()
print_linked_list(reverse_iterative(mylist.head))

head = ListNode(3)
print_linked_list(head)
print_linked_list(reverse_iterative(head))

# test with empty list
print_linked_list(reverse_iterative(LinkedList().head))
print_linked_list(reverse_iterative(ListNode()))
print_linked_list(reverse_iterative())


mylist = LinkedList()
mylist.fromArray([1, 2, 3, 4])
mylist.printList()
head = reverse_recursive(mylist.head)
print_linked_list(head)
