N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]

weight = 0
max_w = 0
parent = [i for i in range(N + 1)]
graph.sort(key=lambda x: x[2])

def find(u):
    if u != parent[u]:
        parent[u] = find(parent[u])
    return parent[u]

def union(u, v):
    r1 = find(u)
    r2 = find(v)
    if r1 != r2:
        parent[r2] = r1


for v1, v2, w in graph:
    if find(v1) != find(v2):
        union(v1, v2)
        weight += w
        max_w = max(w, max_w)

print(weight - max_w)