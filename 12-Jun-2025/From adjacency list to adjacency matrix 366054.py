# Problem: From adjacency list to adjacency matrix - https://basecamp.eolymp.com/en/problems/3982

# example below, replace it with your solution
n = int(input())

matrix = [[0] * n for _ in range(n)]

for i in range(n):
    List = list(map(int, input().split()))

    for j in List[1:]:
        matrix[i][j - 1] = 1

for row in matrix:
    print(*row)
