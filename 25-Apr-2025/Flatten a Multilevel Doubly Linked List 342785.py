# Problem: Flatten a Multilevel Doubly Linked List - https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/?envType=problem-list-v2&envId=linked-list

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        dummy = Node()
        cur = dummy
        stack = [head]

        while stack:
            temp = stack.pop()

            if temp.next:
                stack.append(temp.next)
            if temp.child:
                stack.append(temp.child)
            
            cur.next = temp
            temp.prev = cur
            temp.child = None
            cur = temp
        dummy.next.prev = None
        return dummy.next

        