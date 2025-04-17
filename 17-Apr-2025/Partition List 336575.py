# Problem: Partition List - https://leetcode.com/problems/partition-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        first = ListNode()
        second = ListNode()

        f_last = first
        s_last = second

        while head:
            if head.val < x:
                f_last.next = head
                f_last = f_last.next
            else:
                s_last.next = head
                s_last = s_last.next
            
            head = head.next
        
        f_last.next = second.next
        s_last.next = None

        return first.next
        
    
