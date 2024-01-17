N, S = map(int, input().split())
nums = list(map(int, input().split()))

s, e = 0, 0
l = N + 1
current_sum = 0

while e < N:
    current_sum += nums[e]
    e += 1

    while current_sum >= S:
        l = min(l, e - s)
        current_sum -= nums[s]
        s += 1

print(l if l != N + 1 else 0)
