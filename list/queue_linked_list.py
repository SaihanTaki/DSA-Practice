class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if self.val is None and self.next is None:
            repr = "Empty Node"
        elif self.val is not None:
            repr = f"Node Value = {self.val}, Is Tail Node ? {not bool(self.next)}"
        else:
            repr = f"Not a valid Node, Value = {self.val}, Is Tail Node ? {not bool(self.next)}"
        return repr


# Implementation for Singly Linked List
class LinkedList:
    def __init__(self):
        self.head = ListNode()
        self.tail = self.head

    def __len__(self):
        if self.head.val is None:
            return 0

        len = 1
        curr = self.head
        while curr.next:
            len += 1
            curr = curr.next
        return len

    def insertEnd(self, val):
        if self.head.val is not None:
            self.tail.next = ListNode(val)
            self.tail = self.tail.next
        else:
            self.head = ListNode(val)
            self.tail = self.head

    def fromArray(self, arr):
        for item in arr:
            self.insertEnd(item)

    def toArrary(self):
        arr = []
        if self.head.val is None:
            return arr
        curr = self.head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr

    def getByIndex(self, index):
        if self.head.val is None:
            return None
        if index < 0:
            raise ValueError("Invalid Index")
        i = -1
        curr = self.head
        while curr:
            i += 1
            if index == i:
                return curr.val
            curr = curr.next
        if index > i:
            raise ValueError(
                f"Index = {index} is invalid, possible indexes are ranged from 0 to {self.__len__()}"
            )

    def removeByIndex(self, index):
        if self.head.val is None:
            print("Empty Linked List, Can't delete!")
            return
        i = 0
        curr = self.head
        prev = self.head
        if i == index:
            val = self.head.val
            # case - deleting first element / head
            if self.head.next:
                self.head = self.head.next
            else:
                # case - if head is the only element in the linked list
                self.head = ListNode()
                self.tail = self.head
            return val

        while i < index:
            i += 1
            if curr.val and curr.next:
                # index is in bound
                prev = curr
                curr = curr.next
            else:
                # case - index is out of bound
                print("Index is out of bound!")
                return
        # Remove the node ahead of curr
        if curr.next:
            # case - Deleting in the middle
            prev.next = prev.next.next
        else:
            # case - Deleting the last elemet / tail
            prev.next = None
            self.tail = prev
        return

    def removeByValue(self, value):
        if self.head.val is None:
            return
        while self.head.val == value and self.head:
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = ListNode()
                self.tail = self.head
                return
        prev = self.head
        curr = self.head
        while curr:
            if curr.val == value:
                if curr.next is None:
                    prev.next = None
                    self.tail = prev
                    return
                else:
                    prev.next = prev.next.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return

    def insertAtIndex(self, value, index):
        if self.head.val is None and index == 0:
            # case - index 0, empty list
            self.head = ListNode(value)
            self.tail = self.head
            return
        elif self.head.val is None and index != 0:
            raise ValueError("Empty list. can only insert at index 0")

        i = -1
        curr = self.head
        prev = None
        while curr:
            i += 1
            if index == i:
                next = curr
                curr = ListNode(value)
                curr.next = next
                if prev:
                    # case - index greater than 0, middle to end
                    prev.next = curr
                elif index == 0:
                    # case - index 0, non-empty list
                    self.head = curr
                return
            prev = curr
            curr = curr.next

        if index == i + 1:
            # case - append at the end, index equal to the length of the list
            prev.next = ListNode(value)
            prev.next.next = None
            self.tail = prev.next
            return
        else:
            # case - invalid index, index greater than the length of the list
            raise ValueError(
                f"Index = {index} is invalid, possible indexes are ranged from 0 to {self.__len__()}"
            )

    def printList(self):
        if self.head.val is None:
            print("Empty Linked List")
            return
        curr = self.head
        while curr:
            print(curr.val, end="")
            curr = curr.next
            if curr:
                print(" -> ", end="")
            else:
                print()


class Queue(LinkedList):
    def enqueue(self, value):
        self.insertEnd(value)

    def dequeue(self):
        return self.removeByIndex(0)


myq = Queue()
myq.enqueue(1)
myq.enqueue(2)
myq.enqueue(3)
myq.printList()
myq.dequeue()
myq.printList()
myq.enqueue(4)
myq.printList()
myq.dequeue()
myq.printList()
