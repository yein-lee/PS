from collections import defaultdict
from heapq import heappush, heappop

t = int(input())
for _ in range(t):
    n, d, c = map(int, input().split())
    graph = defaultdict(list)
    for __ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))

    q = [(0, c)]
    distances = [-1] * (n+1)
    distances[c] = 0

    while q:
        current_distance, current_node = heappop(q)

        if distances[current_node] != -1 and distances[current_node] < current_distance:
            continue

        for neighbor_node, weight in graph[current_node]:
            if distances[neighbor_node] == -1 or distances[current_node] + weight < distances[neighbor_node]:
                distances[neighbor_node] = distances[current_node] + weight
                heappush(q, (distances[neighbor_node], neighbor_node))

    cnt = 0
    max_t = 0
    for i in range(1, n+1):
        if distances[i] != -1:
            cnt += 1
        max_t = max(max_t, distances[i])

    print(cnt, max_t)

