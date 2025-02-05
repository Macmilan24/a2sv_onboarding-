# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        dict = {}

        for pair in dislikes:
            if pair[0] in dict:
                dict[pair[0]].add(pair[1])
            else:
                dict[pair[0]] = set([pair[1]])
            if pair[1] in dict:
                dict[pair[1]].add(pair[0])
            else:
                dict[pair[1]] = set([pair[0]])
        
        seen = {}
        for i in range(1, n + 1):
            if i not in seen:
                seen[i] = 0
                stack = [i]
                while stack:
                    a = stack.pop()
                    if a in dict:
                        for b in dict[a]:
                            if b in seen:
                                if seen[a] == seen[b]:
                                    return False
                            else:
                                seen[b] = (seen[a] + 1) % 2
                                stack.append(b)
        return True

            
