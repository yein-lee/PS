t = int(input())
for i in range(t):
    n = int(input())
    workers = [tuple(map(int, input().split())) for _ in range(n)]
    workers.sort()

    cnt = 1
    min_interview = workers[0][1]
    for i in range(1, len(workers)):
        if workers[i][1] < min_interview:
            cnt += 1
            min_interview = workers[i][1]

    print(cnt)
