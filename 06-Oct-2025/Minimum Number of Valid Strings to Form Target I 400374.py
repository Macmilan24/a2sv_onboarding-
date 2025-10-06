# Problem: Minimum Number of Valid Strings to Form Target I - https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/description/

class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]

        n = len(target)
        dp = [float('inf')] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            node = root
            for j in range(i, n):
                char = target[j]
                if char not in node.children:
                    break
                
                node = node.children[char]
                
                if dp[j + 1] != float('inf'):
                    dp[i] = min(dp[i], 1 + dp[j + 1])

        if dp[0] == float('inf'):
            return -1
        else:
            return dp[0]