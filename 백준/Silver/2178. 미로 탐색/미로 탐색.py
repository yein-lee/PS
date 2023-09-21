from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

queue = deque([(1, 0, 0)])  # t x y
visited[0][0] = True
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while queue:
    t, x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and not visited[nx][ny]:
            if nx == n-1 and ny == m-1:
                print(t+1)
                exit(0)

            queue.append((t+1, nx, ny))
            visited[nx][ny] = True
