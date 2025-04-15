# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if index < 0:
            return -1
        temp = self.head
        for _ in range(index):
            if not temp:
                return -1
            temp = temp.next
        return temp.val if temp else -1

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return
        if index == 0:
            self.addAtHead(val)
            return
        cur = self.head
        for _ in range(index - 1):
            if not cur:
                return
            cur = cur.next
        if not cur:
            return
        newNode = Node(val)
        newNode.next = cur.next
        cur.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return
        cur = self.head
        for _ in range(index - 1):
            if not cur:
                return
            cur = cur.next
        if not cur or not cur.next:
            return
        cur.next = cur.next.next