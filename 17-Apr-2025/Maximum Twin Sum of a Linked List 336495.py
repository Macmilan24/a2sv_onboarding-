# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        temp = head
        nums = []
        max_sum = 0

        while temp :
            nums.append(temp.val)
            temp = temp.next
        n = len(nums)
        
        for i in range( n // 2):
            cur_sum = nums[i] + nums[n - 1 - i]
            max_sum = max(max_sum, cur_sum)
        
        return max_sum


        