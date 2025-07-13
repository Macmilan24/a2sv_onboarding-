# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        result_head = lists[0]
        
        for i in range(1, len(lists)):
            current_list = lists[i]

            dummy = ListNode(0)
            merged_tail = dummy
            list1 = result_head
            list2 = current_list

            while list1 and list2:
                if list1.val <= list2.val:
                    merged_tail.next = list1
                    list1 = list1.next
                else:
                    merged_tail.next = list2
                    list2 = list2.next
                merged_tail = merged_tail.next
            
            if list1:
                merged_tail.next = list1
            elif list2:
                merged_tail.next = list2
            
            result_head = dummy.next
        
        return result_head