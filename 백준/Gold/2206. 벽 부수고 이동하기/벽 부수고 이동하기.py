import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
mappp = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visit = [[[0]*2 for _ in range(m)] for _ in range(n)]
visit[0][0][1] = 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque([(0,0,1)])
flag = True
while q:
    x,y,w = q.popleft()
    if x==n-1 and y ==m-1:
        print(visit[x][y][w])
        exit(0)
    for i in range(4):
        x2 = x + dx[i]
        y2 = y + dy[i]
        if 0<=x2<n and 0<=y2<m:
            if mappp[x2][y2]==1 and w==1:
                visit[x2][y2][0] = visit[x][y][1] + 1
                q.append((x2, y2, 0))
            elif mappp[x2][y2]==0 and visit[x2][y2][w]==0:
                visit[x2][y2][w] = visit[x][y][w] + 1
                q.append((x2, y2, w))
print(-1)