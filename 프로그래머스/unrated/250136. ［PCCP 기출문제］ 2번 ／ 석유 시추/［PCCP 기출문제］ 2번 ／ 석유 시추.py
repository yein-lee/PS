from collections import deque


def solution(land):
    n, m = len(land), len(land[0])
    visited = [[0] * m for _ in range(n)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    cnt = 1
    p_dict = dict()
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and land[i][j] == 1:
                p = bfs(i, j, n, m, dx, dy, cnt, land, visited)
                p_dict[cnt] = p
                cnt += 1

    answer = 0
    for j in range(m):
        c_p_set = set()
        p = 0
        for i in range(n):
            if visited[i][j] > 0:
                c_p_set.add(visited[i][j])
        for cnt in c_p_set:
            p += p_dict[cnt]
        answer = max(p, answer)

    return answer


def bfs(x, y, n, m, dx, dy, cnt, graph, visited):
    q = deque([(x, y)])
    visited[x][y] = cnt

    p = 0
    while q:
        x, y = q.popleft()
        p += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = cnt
    return p
    