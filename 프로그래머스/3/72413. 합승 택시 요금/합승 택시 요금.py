def solution(n, s, a, b, fares):
    distances = [[0 if i == j else float('inf') for j in range(n)] for i in range(n)]
    
    for c, d, f in fares:
        distances[c-1][d-1] = f
        distances[d-1][c-1] = f
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
                
    answer = float('inf')
    for i in range(n):
        answer = min(answer, distances[s-1][i] + distances[i][a-1] + distances[i][b-1])
        
    return answer 