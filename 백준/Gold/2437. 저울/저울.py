N = int(input())
weights = list(map(int, input().split()))
weights.sort()

max_measurable = 0
for weight in weights:
    if weight > max_measurable + 1:
        break
    max_measurable += weight

print(max_measurable+1)
