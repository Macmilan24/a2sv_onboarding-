# Problem: Next Greater Node In Linked List - https://leetcode.com/problems/next-greater-node-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        n = len(values)
        result = [0] * n
        stack = []

        for i in range(n):
            while stack and values[i] > values[stack[-1]]:
                prev = stack.pop()
                result[prev] = values[i]
            stack.append(i)

        return result