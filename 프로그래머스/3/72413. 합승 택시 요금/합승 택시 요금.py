from heapq import heappush, heappop
from collections import defaultdict

def solution(n, s, a, b, fares):
    distances = {
        s-1: [float('inf')] * n,
        a-1: [float('inf')] * n,
        b-1: [float('inf')] * n
    }
    
    graph = defaultdict(list)
    for c, d, f in fares:
        graph[c-1].append((d-1, f))
        graph[d-1].append((c-1, f))
    
    q = [(0, s-1)]
    distances[s-1][s-1] = 0
    while q:
        current_distance, current_node = heappop(q)
        if current_distance > distances[s-1][current_node]:
            continue
            
        for neighbor_node, distance in graph[current_node]:
            if current_distance + distance < distances[s-1][neighbor_node]:
                heappush(q, (current_distance + distance, neighbor_node))
                distances[s-1][neighbor_node] = current_distance + distance
                
    q = [(0, a-1)]
    distances[a-1][a-1] = 0
    while q:
        current_distance, current_node = heappop(q)
        if current_distance > distances[a-1][current_node]:
            continue
            
        for neighbor_node, distance in graph[current_node]:
            if current_distance + distance < distances[a-1][neighbor_node]:
                heappush(q, (current_distance + distance, neighbor_node))
                distances[a-1][neighbor_node] = current_distance + distance
                
    q = [(0, b-1)]
    distances[b-1][b-1] = 0
    while q:
        current_distance, current_node = heappop(q)
        if current_distance > distances[b-1][current_node]:
            continue
            
        for neighbor_node, distance in graph[current_node]:
            if current_distance + distance < distances[b-1][neighbor_node]:
                heappush(q, (current_distance + distance, neighbor_node))
                distances[b-1][neighbor_node] = current_distance + distance    
                
    answer = float('inf')
    for i in range(n):
        answer = min(answer, distances[s-1][i] + distances[a-1][i] + distances[b-1][i])
        
    return answer 