import heapq


N = int(input())
cards = [int(input()) for _ in range(N)]
heapq.heapify(cards)

ans = 0
while len(cards) > 1:
    m1 = heapq.heappop(cards)
    m2 = heapq.heappop(cards)
    ans += m1 + m2
    heapq.heappush(cards, m1+m2)

print(ans)
