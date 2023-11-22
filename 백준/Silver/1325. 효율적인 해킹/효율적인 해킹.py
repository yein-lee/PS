import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)

def bfs(x):
    visited = [False for _ in range(n + 1)]
    visited[x]=True
    q = deque([x])
    cnt = 1
    answer = [x]
    while q:
        x = q.popleft()
        for node in graph[x]:
            if not visited[node]:
                visited[node] = True
                q.append(node)
                answer.append(x)
                cnt += 1
    return cnt

max_cnt=0
ans=[]
for i in range(1, n+1):
    temp_cnt = bfs(i)
    if temp_cnt > max_cnt:
        ans = [i]
        max_cnt = temp_cnt
    elif temp_cnt==max_cnt:
        ans.append(i)

for i in range(len(ans)):
    print(ans[i], end=" ")