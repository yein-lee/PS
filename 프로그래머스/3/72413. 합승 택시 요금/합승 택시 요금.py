from heapq import heappop, heappush

    
def solution(n, s, a, b, fares):
    INF = 2e9
    graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
    
    for n1, n2, w in fares:
        graph[n1][n2] = w
        graph[n2][n1] = w

        
    for i in range(1, n+1):
        graph[i][i] = 0

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    answer = INF
    for i in range(1, n+1):
        answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])
                    
    answer = INF
    for i in range(1, n+1):
        answer = min(graph[s][i] + graph[i][a] + graph[i][b], answer)
        
        
    return answer 