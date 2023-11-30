N, X = map(int, input().split())

total_layers = [1]
patties = [1]
for i in range(1, N+1):
    total_layers.append(total_layers[i - 1] * 2 + 3)
    patties.append(patties[i - 1] * 2 + 1)


def patty_in_burger(level, x):
    if level == 0:
        return 0 if x == 0 else 1

    half = total_layers[level-1]

    if x == 1:
        return 0
    elif x <= 1 + half:
        return patty_in_burger(level-1, x-1)
    elif x == 2 + half:
        return patties[level - 1] + 1
    else:
        return patties[level-1] + 1 + patty_in_burger(level-1, x-2-half)

print(patty_in_burger(N, X))
