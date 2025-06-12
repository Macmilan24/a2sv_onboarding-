# Problem: Cities and Roads - https://www.eolymp.com/en/contests/9060/problems/78597

n = int(input())
cities_connection = [list(map(int, input().split())) for _ in range(n)]
roads = 0

for i in range(n):
    for conn in cities_connection[i]:
        roads += conn

roads //= 2
print(roads)