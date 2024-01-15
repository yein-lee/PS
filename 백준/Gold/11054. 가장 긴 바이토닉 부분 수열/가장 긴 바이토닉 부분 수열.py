n = int(input())
sequence = list(map(int, input().split()))

increasing = [1] * n
for i in range(1, n):
    for j in range(i):
        if sequence[j] < sequence[i]:
            increasing[i] = max(increasing[i], increasing[j] + 1)

decreasing = [1] * n
for i in range(n-2, -1, -1):
    for j in range(n-1, i, -1):
        if sequence[j] < sequence[i]:
            decreasing[i] = max(decreasing[i], decreasing[j] + 1)

max_length = 0
for i in range(n):
    max_length = max(max_length, increasing[i] + decreasing[i] - 1)

print(max_length)
