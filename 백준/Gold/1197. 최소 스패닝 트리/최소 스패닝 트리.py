import heapq
from collections import defaultdict


V, E = map(int, input().split())
graph = defaultdict(list)
for _ in range(E):
    e1, e2, w = map(int, input().split())
    graph[e1].append((e2, w))
    graph[e2].append((e1, w))

visited = [False] * (V + 1)
h = [(0, 1)]
answer = 0

while h:
    w, e = heapq.heappop(h)
    if not visited[e]:
        visited[e] = True
        answer += w
        for e2, w in graph[e]:
            if not visited[e2]:
                heapq.heappush(h, (w, e2))

print(answer)

