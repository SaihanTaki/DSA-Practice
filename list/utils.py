def print_linked_list(head):
    if not head:
        print("Empty Linked List")
        return
    elif not head.val and not head.next:
        print("Empty Linked List")
        return
    curr = head
    while curr:
        print(curr.val, end="")
        curr = curr.next
        if curr:
            print(" -> ", end="")
        else:
            print()
