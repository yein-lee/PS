from collections import deque


def solution(n, tops):
    tiles = [0] * (2*n+1)
    for i, top in enumerate(tops):
        if top == 1:
            tiles[i*2+1] = 1

    answer = 0
    stack = [0] 

    while stack:
        current_index = stack.pop()

        if current_index >= 2*n:
            answer += 1
            continue

        if tiles[current_index] == 1:
            stack.append(current_index + 1)
            stack.append(current_index + 1)
            stack.append(current_index + 2)
        elif tiles[current_index] == 0:
            stack.append(current_index + 1)
            stack.append(current_index + 2)
            
    return answer % 10007    
    