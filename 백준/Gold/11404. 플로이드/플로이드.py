n = int(input())
m = int(input())
graph = [[float('inf') for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(c, graph[a-1][b-1])

dist = [[float('inf') for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            dist[i][j] = 0
        elif graph[i][j] != 0:
            dist[i][j] = graph[i][j]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for row in dist:
    print(' '.join(str(0 if x == float('inf') else x) for x in row))
