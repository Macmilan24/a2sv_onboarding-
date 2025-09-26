# Problem: Replace Words - https://leetcode.com/problems/replace-words/

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

    def get_root(self, word: str) -> str:
        node = self.root
        prefix = []
        for ch in word:
            if ch not in node.children:
                return word   
            node = node.children[ch]
            prefix.append(ch)
            if node.is_end:
                return "".join(prefix) 
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for root in dictionary:
            trie.insert(root)

        words = sentence.split()
        replaced = [trie.get_root(word) for word in words]

        return " ".join(replaced)