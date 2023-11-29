N, K = map(int, input().split())
appliances = list(map(int, input().split()))

plugged_in = set()
answer = 0

for i in range(K):
    if appliances[i] in plugged_in:
        continue

    if len(plugged_in) < N:
        plugged_in.add(appliances[i])

    else:
        latest = -1
        for plug in plugged_in:
            if plug not in appliances[i:]:
                to_unplug = plug
                break

            idx = appliances[i:].index(plug)
            if idx > latest:
                latest = idx
                to_unplug = plug

        plugged_in.remove(to_unplug)
        plugged_in.add(appliances[i])
        answer += 1

print(answer)
