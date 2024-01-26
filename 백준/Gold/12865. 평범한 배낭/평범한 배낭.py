import sys
from operator import itemgetter

n, k = map(int, sys.stdin.readline().split())

baggage = []
for i in range(n):
    baggage.append(tuple(map(int, sys.stdin.readline().split())))

def zero_one_kanpsack(cargo):
    pack = []
    global k

    for i in range(len(cargo)+1):
        pack.append([])
        for j in range(k+1):
            if i==0 or j ==0:
                pack[i].append(0)
            elif cargo[i-1][0] <= j:
                pack[i].append(
                    max(cargo[i-1][1]+pack[i-1][j-cargo[i-1][0]],
                        pack[i-1][j])
                )
            else:
                pack[i].append(pack[i-1][j])
    return pack[-1][-1]

print(zero_one_kanpsack(baggage))