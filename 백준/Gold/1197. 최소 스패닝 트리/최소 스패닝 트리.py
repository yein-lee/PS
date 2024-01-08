import heapq
from collections import defaultdict


V, E = map(int, input().split())
graph = defaultdict(list)
for _ in range(E):
    v1, v2, w = map(int, input().split())
    graph[v1].append((v2, w))
    graph[v2].append((v1, w))

visited = set()
min_heap = [(0, 1)]
total_weight = 0

while min_heap:
    w, v1 = heapq.heappop(min_heap)
    if v1 not in visited:
        visited.add(v1)
        total_weight += w

        for v2, w in graph[v1]:
            if v2 not in visited:
                heapq.heappush(min_heap, (w, v2))

print(total_weight)
