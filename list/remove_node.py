from linked_list import LinkedList, print_linked_list


def removeElements(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    if head is None:
        return head

    while head.val == val and head:
        if head.next:
            head = head.next
        else:
            head = None
            return head

    prev = head
    curr = head

    while curr:
        if curr.val == val:
            if curr.next is None:
                prev.next = None
            else:
                prev.next = prev.next.next
            curr = curr.next
        else:
            prev = curr
            curr = curr.next

    return head


# Creating a linked list using LinkedList helper class
mylist = LinkedList()
# mylist.fromArray([3, 3, 1, 2, 3, 4, 3])
mylist.fromArray([3, 3, 3, 3])
# mylist.fromArray([1,3,3,1])
print(len(mylist))
mylist.printList()
head = removeElements(mylist.head, 3)
print_linked_list(head)
