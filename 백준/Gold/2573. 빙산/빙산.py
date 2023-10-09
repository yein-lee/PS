from copy import deepcopy
import sys


sys.setrecursionlimit(100000)

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    # print(x, y)

    cnt = 0
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and graph_copy[nx][ny] == 0:
            cnt += 1
    graph[x][y] = max(graph[x][y] - cnt, 0)

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] > 0 and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny)


t = 0
while True:
    visited = [[False] * M for _ in range(N)]
    graph_copy = deepcopy(graph)
    call_dfs_cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0 and not visited[i][j]:
                # print("dfs start")
                call_dfs_cnt += 1
                visited[i][j] = True
                dfs(i, j)

    # print("call_dfs_cnt", call_dfs_cnt)
    if call_dfs_cnt > 1:
        print(t)
        break

    if call_dfs_cnt == 0:
        print(0)
        break

    t += 1
