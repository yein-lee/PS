from copy import deepcopy

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [-0, 1, 0, -1]
cctv_directions = [
    [],
    [[0], [1], [2], [3]],
    [[1, 3], [0, 2]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]
answer = int(1e9)

cctv_list = []
for i in range(N):
    for j in range(M):
        if 1 <= graph[i][j] <= 5:
            cctv_list.append((i, j, graph[i][j]))


def dfs(pgraph, depth):
    if depth == len(cctv_list):
        global answer
        answer = min(answer, count_zero(pgraph))
        return

    copied_graph = deepcopy(pgraph)
    x, y, cctv_type = cctv_list[depth]
    for cctv_direction in cctv_directions[cctv_type]:
        watch(x, y, cctv_direction, copied_graph)
        dfs(copied_graph, depth + 1)
        copied_graph = deepcopy(pgraph)


def count_zero(pgraph):
    count = 0
    for i in range(N):
        for j in range(M):
            if pgraph[i][j] == 0:
                count += 1
    return count


def watch(x, y, cctv_direction, pgraph):
    for d in cctv_direction:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]

            if nx >=N or nx < 0 or ny >= M or ny < 0 or pgraph[nx][ny] == 6:
                break

            if pgraph[nx][ny] == 0:
                pgraph[nx][ny] = '#'


dfs(graph, 0)
print(answer)
