from math import log2, ceil
from collections import deque


def solution(numbers):
    result = []

    for number in numbers:
        binary_string = format(number, 'b')
        binary_tree_length_binary_number = '0' * (int(2 ** ceil(log2(len(binary_string) + 1))) - 1 - len(binary_string)) + binary_string
        result.append(is_complete_binary_tree(binary_tree_length_binary_number))

    return result


def is_complete_binary_tree(tree):
    if len(tree) == 1:
        return 1
    
    queue = deque([])
    mid_index = len(tree)//2
    queue.append((tree[:mid_index], tree[mid_index]))
    queue.append((tree[mid_index+1:], tree[mid_index]))
    
    while queue:
        tree, parent_node_value = queue.popleft()
        mid_index = len(tree)//2
        if tree[mid_index] == '1' and parent_node_value == '0':
            return 0
        if mid_index == 0:
            continue
        queue.append((tree[:mid_index], tree[mid_index]))
        queue.append((tree[mid_index+1:], tree[mid_index]))
        
    return 1
