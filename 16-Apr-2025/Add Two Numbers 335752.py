# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        cur = temp

        carry = 0

        while l1 or l2 or carry != 0:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            val = num1 + num2 + carry
            carry =  val // 10
            val = val % 10

            cur.next = ListNode(val)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return temp.next