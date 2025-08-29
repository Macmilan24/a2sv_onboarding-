# Problem: Find Kth Largest XOR Coordinate Value - https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/description/?envType=problem-list-v2&envId=bit-manipulation

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        pref = [[0] * (n + 1) for _ in range(m + 1)]
        vals = []

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pref[i][j] = (matrix[i-1][j-1] ^
                              pref[i-1][j] ^
                              pref[i][j-1] ^
                              pref[i-1][j-1])
                vals.append(pref[i][j])

        vals.sort(reverse=True)
        return vals[k-1]