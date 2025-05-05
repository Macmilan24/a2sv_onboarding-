# Problem: Swap Nodes in Pairs - https://leetcode.com/problems/swap-nodes-in-pairs/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        temp = head

        while temp and temp.next:
            next_num = temp.next.next
            sec_num = temp.next
            sec_num.next = temp
            temp.next = next_num
            prev.next = sec_num
            prev = temp
            temp = next_num
        
        return dummy.next