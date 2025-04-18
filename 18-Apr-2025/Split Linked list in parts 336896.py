# Problem: Split Linked list in parts - https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        
        base_size = length // k
        extra = length % k
        
        result = []
        cur = head
        
        for i in range(k):
            part_head = cur
            
            size = base_size + (1 if extra > 0 else 0)

            for j in range(size - 1):
                if cur:
                    cur = cur.next
                    
            if cur:
                next_start = cur.next
                cur.next = None
                cur = next_start
            else:
                cur = None
                
            result.append(part_head)
            
            if extra > 0:
                extra -= 1
        
        return result