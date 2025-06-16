# Problem: Sources and sinks - https://basecamp.eolymp.com/en/problems/3986

# example below, replace it with your solution
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

source = []
sink = []

for i in range(n):
    is_source = True
    is_sink = True

    for j in range(n):
        if matrix[j][i] == 1:
            is_source = False
        if matrix[i][j] == 1:
            is_sink = False
    
    if is_source:
        source.append(i + 1)
    if is_sink:
        sink.append(i + 1)
    
print(len(source), *source)
print(len(sink), *sink)



