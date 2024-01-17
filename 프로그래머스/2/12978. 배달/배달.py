from heapq import heappush, heappop
from collections import defaultdict


def solution(N, road, K):
    graph = defaultdict(list)
    for v1, v2, w in road:
        graph[v1].append((v2, w))
        graph[v2].append((v1, w))

    distances = [float('inf')] * (N + 1)
    distances[1] = 0    
    q = [(0, 1)] # (v, w)
    
    while q:
        current_distance, current_node = heappop(q)
        
        if distances[current_node] < current_distance:
            continue
        
        for neighbor_node, w in graph[current_node]:
            if w + distances[current_node] < distances[neighbor_node]:
                heappush(q, (w + distances[current_node], neighbor_node))
                distances[neighbor_node] = w + distances[current_node]
        
    answer = 0
    for i in range(1, N+1):
        if distances[i] <= K:
            answer += 1
            
    return answer