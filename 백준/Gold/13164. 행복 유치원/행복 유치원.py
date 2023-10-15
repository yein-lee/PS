n, k = map(int, input().split())
heights = list(map(int, input().split()))
heights.sort()

if k >= n:
    print(0)
    exit(0)

distance = []
for i in range(1, n):
    distance.append(heights[i] - heights[i-1])
distance.sort(reverse=True)

print(sum(distance[k-1:]))
