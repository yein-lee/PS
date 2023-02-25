from math import log2, ceil
from collections import deque


def solution(numbers):
    result = []

    for number in numbers:
        binary_string = decimal_int_to_binary_string(number)
        binary_tree_length_binary_number = to_complete_binary_tree_length_string(binary_string)
        if is_complete_binary_tree(binary_tree_length_binary_number) is True:
            result.append(1)
        else:
            result.append(0)
    return result


def decimal_int_to_binary_string(number):
    return format(number, 'b')


def to_complete_binary_tree_length_string(binary_string):
    return '0' * (int(2 ** ceil(log2(len(binary_string) + 1))) - 1 - len(binary_string)) + binary_string


def is_complete_binary_tree(tree):
    if len(tree) == 1:
        return True
    
    queue = deque([])
    mid_index = len(tree)//2
    queue.append((tree[:mid_index], tree[mid_index]))
    queue.append((tree[mid_index+1:], tree[mid_index]))
    while queue:
        tree, parent_node_value = queue.popleft()
        mid_index = len(tree)//2
        if tree[mid_index] == '1' and parent_node_value == '0':
            return False
        if mid_index == 0:
            continue
        queue.append((tree[:mid_index], tree[mid_index]))
        queue.append((tree[mid_index+1:], tree[mid_index]))
    return True

