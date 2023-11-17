from heapq import heappush, heappop
from collections import defaultdict


INF = float('inf')
graph = defaultdict(list)
N, M = map(int, input().split())

for _ in range(M):
    e1, e2, w = map(int, input().split())
    graph[e1].append((e2, w))
    graph[e2].append((e1, w))

visited = [False] * (N+1)
distances = [INF] * (N+1)
distances[1] = 0
for e, w in graph[1]:
    distances[e] = w

q = [(0, 1)]
while q:
    d, e = heappop(q)
    if not visited[e]:
        visited[e] = True
        for ne, w in graph[e]:
            if not visited[ne]:
                distances[ne] = min(distances[ne], distances[e] + w)
                heappush(q, (distances[ne], ne))

print(distances[-1])
