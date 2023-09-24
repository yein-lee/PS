negatives = []
positives = []

N = int(input())
answer = 0
for _ in range(N):
    t = int(input())
    if t > 1:
        positives.append(t)
    elif t <= 0:
        negatives.append(t)
    elif t == 1:
        answer += t


positives.sort(reverse=True)
negatives.sort()

if len(positives) % 2 == 0:
    for i in range(0, len(positives), 2):
        answer += positives[i] * positives[i+1]
else:
    for i in range(0, len(positives)-1, 2):
        answer += positives[i] * positives[i + 1]
    answer += positives[-1]

if len(negatives) % 2 == 0:
    for i in range(0, len(negatives), 2):
        answer += negatives[i] * negatives[i+1]
else:
    for i in range(0, len(negatives)-1, 2):
        answer += negatives[i] * negatives[i + 1]
    answer += negatives[-1]

print(answer)