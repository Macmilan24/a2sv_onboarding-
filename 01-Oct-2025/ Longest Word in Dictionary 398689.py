# Problem:  Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word = ""   # store the full word when ending here

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
        node.word = word

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for w in words:
            trie.insert(w)

        best = ""

        def dfs(node):
            nonlocal best
            if node.word:
             
                if len(node.word) > len(best) or (len(node.word) == len(best) and node.word < best):
                    best = node.word

            for ch in sorted(node.children.keys()): 
                child = node.children[ch]
                if child.is_end:  
                    dfs(child)

        dfs(trie.root)
        return best