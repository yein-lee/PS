from heapq import heappush, heappop

N = int(input())
lectures = [list(map(int, input().split())) for _ in range(N)]
lectures.sort()

heap = []
cnt = 0
for s, e in lectures:
    while heap and heap[0] <= s:
        heappop(heap)
    heappush(heap, e)
    cnt = max(cnt, len(heap))

print(cnt)