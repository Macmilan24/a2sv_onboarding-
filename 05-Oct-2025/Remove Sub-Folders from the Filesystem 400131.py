# Problem: Remove Sub-Folders from the Filesystem - https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = TrieNode()

        folder.sort()

        result = []

        for path in folder:
            node = root
            parts = path.split('/')[1:]  
            is_subfolder = False

            for part in parts:
                if part not in node.children:
                    node.children[part] = TrieNode()
                node = node.children[part]
                if node.is_end:
                    is_subfolder = True
                    break

            if not is_subfolder:
                node.is_end = True
                result.append(path)

        return result