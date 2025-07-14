# Problem: E - The Case of the Missing Operations - https://codeforces.com/gym/622136/problem/E

import heapq


def solve():
    n = int(input())

    heap = []
    res = []

    for _ in range(n):
        line = input()

        if line.startswith("insert"):
            val = int(line.split()[1])
            heapq.heappush(heap, val)
            res.append(line)
        elif line.startswith("removeMin"):
            if not heap:
                res.append("insert 0")
            else:
                heapq.heappop(heap)
            res.append(line)
        else:
            val = int(line.split()[1])
            while heap and heap[0] < val:
                heapq.heappop(heap)
                res.append("removeMin")

            if not heap or heap[0] > val:
                heapq.heappush(heap, val)
                res.append(f"insert {val}")

            res.append(line)

    print(len(res))
    for result in res:
        print(result)


solve()
