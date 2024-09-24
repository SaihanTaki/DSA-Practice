class ListNode:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class DoublyLinkedList:
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

    def append(self, value):
        if self.head.val is None:
            self.head.val = value
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = ListNode(value)
            curr.next.prev = curr
        return

    def prepend(self, value):
        if self.head.val is None:
            self.head.val = value
            return
        newHead = ListNode(value)
        newHead.next = self.head
        self.head.prev = newHead
        self.head = newHead

    def insertByIndex(self, index, value):
        if index < 0 or index > self.__len__():
            raise ValueError(f"Invalid Index")
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

    def removeByIndex(self, index):
        if self.head.val is None:
            print("Empty Linked List, Can't delete!")
            return
        if index < 0 or index >= self.__len__():
            raise ValueError(f"Invalid Index")

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

    def getByIndex(self, index):
        if self.head.val is None:
            print("Empty Linked List!")
            return
        if index < 0 or index >= self.__len__():
            raise ValueError(f"Invalid Index")

        i = 0
        curr = self.head
        while curr:
            if index == i:
                return curr.val
            i += 1
            curr = curr.next

    def toArray(self):
        array = []
        if self.head.val is None:
            return array

        curr = self.head
        while curr:
            array.append(curr.val)
            curr = curr.next
        return array

    def fromArray(self, array):
        for value in array:
            self.append(value)

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


mylist = DoublyLinkedList()
print(mylist.__len__())
mylist.insertByIndex(0, 5)
mylist.prepend(4)
mylist.append(1)
mylist.prepend(3)
print(mylist.__len__())
mylist.append(2)
mylist.insertByIndex(5, 3)
print(mylist.__len__())
mylist.printList()
mylist.removeByIndex(3)
mylist.printList()
print(mylist.getByIndex(4))
print(mylist.getByIndex(2))
print(mylist.getByIndex(0))
print(mylist.toArray())
mylist.fromArray([9, 7])
mylist.printList()
print(mylist.toArray())
