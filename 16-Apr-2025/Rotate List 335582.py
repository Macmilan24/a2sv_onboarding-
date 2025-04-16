# Problem: Rotate List - https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        length = 1
        last = head

        while last.next:
            last = last.next
            length += 1
        
        k = k % length
        temp = head
        for _ in range(length - k - 1):
            temp = temp.next
            
        last.next = head
        head = temp.next
        temp.next = None

        return head

        
        

        