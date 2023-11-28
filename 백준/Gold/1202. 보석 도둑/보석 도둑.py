import heapq


N, K = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

jewels.sort()
bags.sort()

available_jewels = []
max_value = 0
jewel_idx = 0

for bag in bags:
    while jewel_idx < N and jewels[jewel_idx][0] <= bag:
        heapq.heappush(available_jewels, -jewels[jewel_idx][1])
        jewel_idx += 1

    if available_jewels:
        max_value -= heapq.heappop(available_jewels)

print(max_value)
