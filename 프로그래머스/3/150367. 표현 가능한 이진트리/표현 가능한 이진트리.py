from math import log2, ceil
from collections import deque


def solution(numbers):
    result = []

    for number in numbers:
        binary = to_binary_string(number)
        full_binary = to_full_binary_tree(binary)
        result.append(1 if is_binary_tree_representable(full_binary) else 0)

    return result


def to_binary_string(number):
    reversed_binary = []
    while number:
        reversed_binary.append(number%2)
        number //= 2
    return ''.join(map(str, reversed(reversed_binary)))


def to_full_binary_tree(s):
    k = ceil(log2(len(s) + 1))
    
    goal_length = 2 ** k - 1
    lack_length = goal_length - len(s)
    
    return "0" * lack_length + s


def is_binary_tree_representable(s):
    q = deque([])
    m = len(s)//2
    q.append((s[m], s[:m]))
    q.append((s[m], s[m+1:]))

    while q:
        p, s = q.popleft()
        m = len(s) // 2
        if p == '0' and s[m] == '1':
            return False
        if len(s) > 1:
            q.append((s[m], s[:m]))
            q.append((s[m], s[m+1:]))
    return True
