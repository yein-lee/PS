G = int(input())
P = int(input())
planes = [int(input()) for _ in range(P)]

parent = [i for i in range(G+1)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

answer = 0
for plane in planes:
    root = find_parent(parent, plane)
    if root == 0:
        break

    union_parent(parent, root, root - 1)
    answer += 1

print(answer)