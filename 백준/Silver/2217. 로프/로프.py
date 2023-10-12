N = int(input())
W = []
for _ in range(N):
    W.append(int(input()))
W.sort()

answer = 0
for i in range(N):
    t = (N-i) * W[i]
    if t > answer:
        answer = t

print(answer)
