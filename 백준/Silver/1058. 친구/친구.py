N = int(input())
graph = [list(input()) for _ in range(N)]
friend = [[0 for _ in range(N)] for _ in range(N)]


for i in range(N):
    for j in range(N):
        if graph[i][j] == 'Y':
            friend[i][j] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i!=j and graph[i][k] == 'Y' and graph[k][j] == 'Y':
                friend[i][j] = 1

max_n = 0
for i in range(N):
    n = sum(friend[i])
    max_n = max(max_n, n)
print(max_n)
