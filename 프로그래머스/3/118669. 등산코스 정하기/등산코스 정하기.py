from collections import defaultdict
from heapq import heapify, heappush, heappop


def solution(n, paths, gates, summits):
    graph = defaultdict(list)
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))
        
    intensities = [1e10] * (n + 1)
    q = []
    for g in gates:
        intensities[g] = 0
        heappush(q, (0, g))
    
    while q:
        i, e = heappop(q)
        
        if intensities[e] < i or e in summits:
            continue
        
        for ne, ni in graph[e]:
            max_i = max(i, ni)
            if intensities[ne] > max_i:
                intensities[ne] = max_i
                heappush(q, (max_i, ne))
        
    answer = [-1, 1e10]
    for s in summits:
        if intensities[s] < answer[1] or intensities[s] == answer[1] and s < answer[0]:
            answer[0], answer[1] = s, intensities[s]

    return answer
                