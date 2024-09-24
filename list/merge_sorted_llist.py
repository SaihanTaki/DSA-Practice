from linked_list import LinkedList, ListNode, print_linked_list


def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    head = ListNode()
    curr = head

    while list1 and list2:
        if list1.val > list2.val:
            curr.next = list2
            list2 = list2.next
        else:
            curr.next = list1
            list1 = list1.next
        curr = curr.next
    curr.next = list1 or list2

    return head.next


list1 = LinkedList()
list1.fromArray([1, 2, 5, 9])
list2 = LinkedList()
list2.fromArray([4, 5, 6])

ms_list = mergeTwoLists(list1.head, list2.head)

print_linked_list(ms_list)
