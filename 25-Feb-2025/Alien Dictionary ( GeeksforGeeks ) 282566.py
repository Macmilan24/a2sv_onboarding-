# Problem: Alien Dictionary ( GeeksforGeeks ) - https://www.geeksforgeeks.org/problems/alien-dictionary/1

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import sys


# } Driver Code Ends

#User function Template for python3
from collections import defaultdict, deque
class Solution:
    def findOrder(words):
        graph = defaultdict(set)
        in_degree = {}
        chars = set()
    
        for word in words:
            for c in word:
                chars.add(c)
                in_degree[c] = 0
    
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        in_degree[w2[j]] = in_degree.get(w2[j], 0) + 1
                    break
            else:
                if len(w1) > len(w2):
                    return ""
    
        queue = deque([c for c in chars if in_degree[c] == 0])
        result = []
    
        while queue:
            curr = queue.popleft()
            result.append(curr)
            for neighbor in graph[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
    
        return "".join(result) if len(result) == len(chars) else ""


#{ 
 # Driver Code Starts.

def validate(original, order):
    char_map = {}
    for word in original:
        for ch in word:
            char_map[ch] = 1

    for ch in order:
        if ch not in char_map:
            return False
        del char_map[ch]

    if char_map:
        return False

    char_index = {ch: i for i, ch in enumerate(order)}

    for i in range(len(original) - 1):
        a, b = original[i], original[i + 1]
        k, n, m = 0, len(a), len(b)
        while k < n and k < m and a[k] == b[k]:
            k += 1
        if k < n and k < m and char_index[a[k]] > char_index[b[k]]:
            return False
        if k != n and k == m:
            return False

    return True

if __name__ == "__main__":
    input_data = sys.stdin.read().strip().split("\n")
    index = 0
    t = int(input_data[index])
    index += 1
    while t > 0:
        words = input_data[index].split()
        index += 1
        original = words[:]

        order = Solution.findOrder(words)

        if order == "":
            print("\"\"")
        else:
            print("true" if validate(original, order) else "false")
        print("~")
        t -= 1

# } Driver Code Ends