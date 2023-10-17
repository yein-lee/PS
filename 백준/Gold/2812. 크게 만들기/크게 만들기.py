N, K = map(int, input().split())
numbers = list(map(int, input()))

stack = []

for number in numbers:
    while stack and stack[-1] < number and K > 0:
        stack.pop()
        K -= 1
    stack.append(number)

if K > 0:
    stack = stack[:-K]

print(''.join(map(str, stack)))