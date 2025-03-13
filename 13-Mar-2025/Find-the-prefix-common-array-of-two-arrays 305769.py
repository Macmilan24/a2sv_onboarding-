# Problem: Find-the-prefix-common-array-of-two-arrays - https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        prefix_count = [0] * len(A)
        seen_A = set()
        seen_B = set()

        for i in range(len(A)):
            seen_A.add(A[i])
            seen_B.add(B[i])

            if i > 0:
                prefix_count[i] = prefix_count[i - 1]
            
            if A[i] in seen_B:
                prefix_count[i] += 1
            if B[i] in seen_A and B[i] != A[i]:
                prefix_count[i] += 1
        
        return prefix_count