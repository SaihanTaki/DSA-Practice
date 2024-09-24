class ListNode:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:

    def __init__(self):
        self.head = ListNode()

    def __len__(self):
        if self.head.val is None:
            return 0
        length = 1
        curr = self.head
        while curr.next:
            length += 1
            curr = curr.next
        return length

    def get(self, index: int) -> int:
        if self.head.val is None:
            print("Empty Linked List!")
            return
        if index < 0 or index >= self.__len__():
            print(f"Invalid Index")
            return -1

        i = 0
        curr = self.head
        while curr:
            if index == i:
                return curr.val
            i += 1
            curr = curr.next

    def addAtHead(self, value: int) -> None:
        if self.head.val is None:
            self.head.val = value
            return
        newHead = ListNode(value)
        newHead.next = self.head
        self.head.prev = newHead
        self.head = newHead

    def addAtTail(self, value: int) -> None:
        if self.head.val is None:
            self.head.val = value
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = ListNode(value)
            curr.next.prev = curr
        return

    def addAtIndex(self, index: int, value: int) -> None:
        if index < 0 or index > self.__len__():
            print(f"Invalid Index")
        if index == 0:
            if self.head.val is None:
                self.head.val = value
            else:
                newNode = ListNode(value)
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            return

        i = 0
        curr = self.head
        while curr.next:
            i += 1
            if index == i:
                newNode = ListNode(value)
                nextNode = curr.next
                curr.next = newNode
                newNode.prev = curr
                newNode.next = nextNode
                nextNode.prev = newNode
                return
            curr = curr.next

        if index == i + 1:
            newNode = ListNode(value)
            newNode.prev = curr
            curr.next = newNode
            return

    def deleteAtIndex(self, index: int) -> None:
        if self.head.val is None:
            print("Empty Linked List, Can't delete!")
            return
        if index < 0 or index >= self.__len__():
            print("Invalid Index")
            return

        if index == 0:
            if self.head.next is None:
                self.head = ListNode()
            else:
                nextNode = self.head.next
                nextNode.prev = None
                self.head = nextNode
            return
        else:
            i = 0
            curr = self.head
            while curr.next:
                if index == i:
                    nextNode = curr.next
                    prevNode = curr.prev
                    prevNode.next = nextNode
                    nextNode.prev = prevNode
                    return
                i += 1
                curr = curr.next

        if index == i:
            prevNode = curr.prev
            prevNode.next = None
        return


mylist = MyLinkedList()
mylist.addAtHead(1)
mylist.addAtTail(3)
mylist.addAtIndex(1, 2)
print(mylist.get(1))
mylist.deleteAtIndex(1)
print(mylist.get(1))
