# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        temp = head
        length = 0

        while temp:
            temp = temp.next
            length += 1
        
        prev = head

        k = length - n - 1

        if k == -1:
            return head.next

        for _ in range(k):
            prev = prev.next
        
        prev.next = prev.next.next

        return head
