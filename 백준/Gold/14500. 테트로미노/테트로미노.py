N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

max_w = 0


def dfs(cw, clist):
    if len(clist) == 4:
        global max_w
        max_w = max(cw, max_w)
        return

    for x ,y in clist:
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in clist:
                clist.append((nx, ny))
                dfs(cw + graph[nx][ny], clist)
                clist.pop()


for i in range(N):
    for j in range(M):
       dfs(graph[i][j], [(i, j)])


print(max_w)
