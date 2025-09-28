# Problem: Shortest Uncommon Substring in an Array - https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = set() 
class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        root = TrieNode()
        n = len(arr)

        for idx, word in enumerate(arr):
            m = len(word)
            for start in range(m): 
                node = root
                for j in range(start, m):
                    ch = word[j]
                    if ch not in node.children:
                        node.children[ch] = TrieNode()
                    node = node.children[ch]
                    node.words.add(idx)
        result = []
        for idx, word in enumerate(arr):
            best = None
            m = len(word)
            for length in range(1, m + 1):  
                candidates = []
                for start in range(m - length + 1):
                    sub = word[start : start + length]
                  
                    node = root
                    ok = True
                    for ch in sub:
                        if ch not in node.children:
                            ok = False
                            break
                        node = node.children[ch]
                    if ok and node.words == {idx}:  
                        candidates.append(sub)

                if candidates:
                    best = min(candidates)  
                    break

            if best is None:
                result.append("")
            else:
                result.append(best)

        return result