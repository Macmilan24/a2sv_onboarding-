# Problem: Delete Duplicate Folders in System - https://leetcode.com/problems/delete-duplicate-folders-in-system/description/

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.deleted = False
        self.key = ""

class Solution:
    def deleteDuplicateFolder(self, paths: list[list[str]]) -> list[list[str]]:
        root = TrieNode()
        for path in paths:
            node = root
            for folder in path:
                node = node.children[folder]
        
        seen = collections.defaultdict(list)
        
        def serialize(node):
            if not node.children:
                return ""
            
            sub_keys = []
            for name in sorted(node.children.keys()):
                sub_keys.append(name + "(" + serialize(node.children[name]) + ")")
            
            key = "".join(sub_keys)
            seen[key].append(node)
            node.key = key
            return key

        serialize(root)
        
        for key in seen:
            if len(seen[key]) > 1:
                for node in seen[key]:
                    node.deleted = True
        
        result = []
        
        def build_path(node, current_path):
            if node.deleted:
                return
            
            if current_path:
                result.append(current_path)
            
            for name in sorted(node.children.keys()):
                build_path(node.children[name], current_path + [name])

        build_path(root, [])
        return result