N = int(input())
tasks = [tuple(map(int, input().split())) for _ in range(N)] # (d, w)


tasks.sort(key=lambda x: -x[1])
max_day = max(task[0] for task in tasks)
days = [False] * (max_day + 1)

answer = 0
for d, w in tasks:
    for i in range(d, 0, -1):
        if not days[i]:
            days[i] = True
            answer += w
            break

print(answer)
