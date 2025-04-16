# Problem: Middle of the Linked List - https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        length = 1
        last = head

        while last.next:
            last = last.next
            length += 1

        temp = head
        for _ in range(length // 2):
            temp = temp.next
        
        return temp
