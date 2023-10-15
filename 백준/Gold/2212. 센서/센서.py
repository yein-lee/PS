n = int(input())
k = int(input())
sensors = list(map(int, input().split()))
sensors.sort()

if k >= n:
    print(0)
    exit(0)

distance = []
for i in range(1, n):
    distance.append(sensors[i] - sensors[i-1])
distance.sort(reverse=True)

print(sum(distance[k-1:]))
