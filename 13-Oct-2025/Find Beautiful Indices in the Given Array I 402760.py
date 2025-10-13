# Problem: Find Beautiful Indices in the Given Array I - https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/description/

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        n = len(s)
        len_a = len(a)
        len_b = len(b)

        a_indices = []
        for i in range(n - len_a + 1):
            if s[i:i + len_a] == a:
                a_indices.append(i)

        b_indices = []
        for i in range(n - len_b + 1):
            if s[i:i + len_b] == b:
                b_indices.append(i)

        result = []
        if not b_indices:
            return result
            
        for i in a_indices:
            
            left_bound = i - k
            right_bound = i + k
            
            
            insertion_point = bisect.bisect_left(b_indices, left_bound)
            
            
            if insertion_point < len(b_indices):
                j = b_indices[insertion_point]
                if j <= right_bound:
                    result.append(i)

        return result