graph = [list(map(int, list(input()))) for _ in range(9)]

zeros = []
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            zeros.append((i,j))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def check_row(x, y, n):
    for i in range(9):
        if graph[x][i] == n:
            return False
    return True


def check_column(x, y, n):
    for i in range(9):
        if graph[i][y] == n:
            return False
    return True


def check_square(x, y, n):
    nx = (x//3) * 3
    ny = (y//3) * 3
    for i in range(3):
        for j in range(3):
            if graph[nx+i][ny+j] == n:
                return False
    return True


def dfs(depth):
    if depth == len(zeros):
        for i in range(9):
            print(''.join(map(str, graph[i])))
        exit(0)

    x, y = zeros[depth]

    for i in range(1, 10):
        if check_row(x,y,i) and check_column(x,y,i) and check_square(x,y,i):
            graph[x][y] = i
            dfs(depth + 1)
            graph[x][y] = 0

dfs(0)

