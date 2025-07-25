# Problem: Find K Pairs with Smallest Sums - https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        
        min_heap = [(nums1[0] + nums2[0], 0, 0)]  # (sum, i, j)
        visited = {(0, 0)}
        result = []
        
        while k > 0 and min_heap:
            current_sum, i, j = heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            
            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))
            
            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))
            
            k -= 1
        
        return result