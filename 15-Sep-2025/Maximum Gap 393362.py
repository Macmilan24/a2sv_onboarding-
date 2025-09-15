# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/description/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        minVal, maxVal = min(nums), max(nums)
        if minVal == maxVal:
            return 0

        bucketSize = math.ceil((maxVal - minVal) / (n - 1))
        bucketCount = (maxVal - minVal) // bucketSize + 1

        minBucket = [float("inf")] * bucketCount
        maxBucket = [float("-inf")] * bucketCount
        used = [False] * bucketCount

        for num in nums:
            idx = (num - minVal) // bucketSize
            minBucket[idx] = min(minBucket[idx], num)
            maxBucket[idx] = max(maxBucket[idx], num)
            used[idx] = True

        prevMax = minVal
        maxGap = 0
        for i in range(bucketCount):
            if not used[i]:
                continue
            maxGap = max(maxGap, minBucket[i] - prevMax)
            prevMax = maxBucket[i]

        return maxGap