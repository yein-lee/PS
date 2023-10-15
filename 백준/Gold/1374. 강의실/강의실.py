from heapq import heappush, heappop


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key=lambda x: x[1])
heap = []
count = 0

for class_n, start, end in arr:
    while heap and heap[0] <= start:
        heappop(heap)
    heappush(heap, end)
    count = max(count, len(heap))

print(count)
