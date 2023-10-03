from collections import defaultdict


N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [False] * N


def dfs(v, depth):
    if depth == 5:
        print(1)
        exit(0)

    for v2 in graph[v]:
        if not visited[v2]:
            visited[v2] = True
            dfs(v2, depth + 1)
            visited[v2] = False


for i in range(N):
    visited[i] = True
    dfs(i, 1)
    visited[i] = False

print(0)
