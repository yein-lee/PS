from collections import defaultdict


def dfs(graph, stack, visited):
    while stack:
        v = stack.pop()

        for a in graph[v]:
            if visited[a] == 0:
                stack.append(a)
                visited[a] = - visited[v]
            else:
                if visited[a] == visited[v]:
                    return False
    return True


K = int(input())
for _ in range(K):
    V, E = map(int, input().split())  # 정점, 간선
    graph = defaultdict(list)
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (V + 1)
    stack = []

    for v in graph.keys():
        if visited[v] == 0:
            stack.append(v)
            visited[v] = 1
            result = dfs(graph, stack, visited)

            if not result:
                print("NO")
                break

    if result:
        print("YES")
