# Problem: Copy List with Random Pointer - https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        cur = head
        while cur:
            cp = Node(cur.val, cur.next,None)
            cur.next = cp
            cur = cp.next
        
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        cur = head
        N_head = head.next
        while cur:
            cp = cur.next
            cur.next = cp.next
            cur = cur.next
            if cp.next:
                cp.next = cp.next.next
        
        return N_head