# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode(0, head)
        prev = temp
        last = head

        while n > 0 and last:
            last = last.next
            n -= 1
        
        while last:
            prev = prev.next
            last = last.next
        
        prev.next = prev.next.next

        return temp.next
