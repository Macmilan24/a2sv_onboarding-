# Problem: Maximum XOR With an Element From Array - https://leetcode.com/problems/maximum-xor-with-an-element-from-array/description/

class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]

    def find_max_xor(self, num):
        if not self.root.children:
            return -1
        
        node = self.root
        max_xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            opposite_bit = 1 - bit
            
            if opposite_bit in node.children:
                max_xor |= (1 << i)
                node = node.children[opposite_bit]
            else:
                node = node.children[bit]
        return max_xor

class Solution:
    def maximizeXor(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        nums.sort()
        
        indexed_queries = []
        for i, query in enumerate(queries):
            indexed_queries.append(query + [i])
        
        indexed_queries.sort(key=lambda x: x[1])
        
        ans = [-1] * len(queries)
        trie = Trie()
        nums_idx = 0
        
        for x, m, original_idx in indexed_queries:
            while nums_idx < len(nums) and nums[nums_idx] <= m:
                trie.insert(nums[nums_idx])
                nums_idx += 1
            
            ans[original_idx] = trie.find_max_xor(x)
            
        return ans