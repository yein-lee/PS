import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
houses = []
chickens = []

for i in range(n):
    for j in range(n):
        if map[i][j]==1:
            houses.append((i,j))
        elif map[i][j]==2:
            chickens.append((i,j))



min = int(1e9)
for chickens_comb in combinations(chickens, m):
    sum = 0
    for house in houses:
        min_chicken_distance = int(1e9)
        for chicken in chickens_comb:
            if abs(house[0]-chicken[0]) + abs(house[1]- chicken[1])<min_chicken_distance:
                min_chicken_distance = abs(house[0]-chicken[0]) + abs(house[1]- chicken[1])
        sum += min_chicken_distance
    if sum < min:
        min = sum

print(min)

# print(combinations(chickens,m))
# for chickens_comb in combinations(chickens, m):
#     for chickens in chickens_comb:
#         print(chickens)