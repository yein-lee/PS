sudoku = [list(map(int, input().split())) for _ in range(9)]

empty = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            empty.append((i,j))


def row(x, n):
    for i in range(9):
        if sudoku[x][i] == n:
            return False
    return True


def column(y, n):
    for i in range(9):
        if sudoku[i][y] == n:
            return False
    return True


def square(x, y, n):
    a = x // 3 * 3
    b = y //3 * 3
    for i in range(3):
        for j in range(3):
            if sudoku[a+i][b+j] == n:
                return False
    return True


def dfs(depth):
    if depth == len(empty):
        for i in range(9):
            print(' '.join(map(str, sudoku[i])))
        exit(0)

    x, y = empty[depth]

    for i in range(1, 10):
        if row(x, i) and column(y, i) and square(x, y, i):
            sudoku[x][y] = i
            dfs(depth + 1)
            sudoku[x][y] = 0

dfs(0)