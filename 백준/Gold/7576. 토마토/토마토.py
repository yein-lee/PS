import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split()) #[n][m]
tomatoes = list()
for i in range(n):
    tomatoes.append(list(map(int, sys.stdin.readline().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, q):
    result=1
    while(q):
        x, y = q.popleft()
        # print("popleft ", x, y)
        for i in range(4):
            x2 = x + dx[i]
            y2 = y + dy[i]
            # print("x2, y2: ", x2, y2)
            if(0<=x2<n and 0<=y2<m and graph[x2][y2]==0):
                # print("append", x2, y2)
                q.append([x2, y2])
                graph[x2][y2] = graph[x][y] + 1
                temp = graph[x2][y2]
                if(temp>result):
                    result = temp
    return result

q = deque([])
for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 1:
            q.append([i,j])
# print(q)
# print(tomatoes)
result = bfs(tomatoes, q)
for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 0:
            print(-1)
            exit()

print(result-1)