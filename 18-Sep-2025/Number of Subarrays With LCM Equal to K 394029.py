# Problem: Number of Subarrays With LCM Equal to K - https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        
        for i in range(n):
            l = 1
            for j in range(i, n):
                if k % nums[j] != 0:
                    break
                
                l = (l * nums[j]) // math.gcd(l, nums[j])
                
                if l == k:
                    ans += 1
                elif l > k: 
                    break
        return ans