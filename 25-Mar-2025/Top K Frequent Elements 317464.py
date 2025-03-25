# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        element_count = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1) ]
        res = []

        for num, count in element_count.items():
            freq[count].append(num)
        
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        