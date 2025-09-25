# Problem: Word Break - https://leetcode.com/problems/word-break/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        memo = {}

        def dfs(start):
            if start == len(s):
                return True
            if start in memo:
                return memo[start]

            node = trie.root
            for i in range(start, len(s)):
                ch = s[i]
                if ch not in node.children:
                    break
                node = node.children[ch]
                if node.is_end and dfs(i + 1):
                    memo[start] = True
                    return True

            memo[start] = False
            return False

        return dfs(0)