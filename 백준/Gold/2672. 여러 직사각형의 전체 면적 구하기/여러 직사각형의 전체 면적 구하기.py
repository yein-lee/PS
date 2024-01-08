N = int(input())
rectangles = []
for _ in range(N):
    x, y, w, h = map(float, input().split())
    rectangles.append([x, y, y+h, 1])
    rectangles.append([x+w, y, y+h, -1])
rectangles.sort()

area = 0
y_list = [0] * 25001

for i in range(len(rectangles) - 1):
    x, y1, y2, flag = rectangles[i]
    y1 = int(y1 * 10)
    y2 = int(y2 * 10)

    if flag == 1:
        for j in range(y1, y2):
            y_list[j] += 1
    elif flag == -1:
        for j in range(y1, y2):
            y_list[j] -= 1

    area += (rectangles[i+1][0] - x) * (sum(1 for e in y_list if e != 0) / 10)

if area - int(area) > 0:
    print(f'{area:0.2f}')
else:
    print(int(area))
