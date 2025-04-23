# Problem: Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []

        while l1:
            num1.append(l1.val)
            l1 = l1.next
        while l2:
            num2.append(l2.val)
            l2 = l2.next
        

        total_sum = 0
        carry = 0
        res = ListNode()

        while len(num1) > 0 or len(num2) > 0:
            if num1:
                total_sum += num1.pop()
            
            if num2:
                total_sum += num2.pop()
            
            res.val = total_sum % 10
            carry = total_sum // 10
            head = ListNode(carry)
            head.next = res
            res = head
            total_sum = carry

        if carry == 0:
            return res.next
        else:
            return res
