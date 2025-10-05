# Problem: Short Encoding of Words - https://leetcode.com/problems/short-encoding-of-words/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_leaf = True

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words))
        
        root = TrieNode()
        
        for word in words:
            node = root
            for ch in reversed(word):
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                    node.is_leaf = False
                node = node.children[ch]
        
        def dfs(node, depth):
            if not node.children:
                return depth + 1  
            total = 0
            for child in node.children.values():
                total += dfs(child, depth + 1)
            return total
        
        return dfs(root, 0)