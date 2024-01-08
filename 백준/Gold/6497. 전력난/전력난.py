import heapq
from collections import defaultdict


while True:
    V, E = map(int, input().split())
    if V == 0 and E == 0:
        break

    graph = defaultdict(list)
    total_weight = 0
    for _ in range(E):
        v1, v2, w = map(int, input().split())
        total_weight += w
        graph[v1].append((v2, w))
        graph[v2].append((v1, w))

    visited = set()
    min_heap = [(0, v1)]
    mst_weight = 0

    while min_heap:
        w, v1 = heapq.heappop(min_heap)
        if v1 not in visited:
            visited.add(v1)
            mst_weight += w

            for v2, w in graph[v1]:
                if v2 not in visited:
                    heapq.heappush(min_heap, (w, v2))

    print(total_weight - mst_weight)