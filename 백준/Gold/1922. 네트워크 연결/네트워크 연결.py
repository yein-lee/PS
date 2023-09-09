N = int(input())
M = int(input())

edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()
parent = [i for i in range(N+1)]
rank = [0 for _ in range(N+1)]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_x] = root_y
            rank[root_y] += 1


mst = []
cost = 0

for edge in edges:
    w, u, v = edge
    if find(u) != find(v):
        union(u, v)
        cost += w

print(cost)
