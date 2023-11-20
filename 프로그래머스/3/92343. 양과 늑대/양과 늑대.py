from collections import defaultdict


def solution(info, edges):
    binary_tree = defaultdict(list)
    for p, c in edges:
        binary_tree[p].append(c)

    answer = 0
    stack = [([0], 0, 0)]
    
    while stack:
        nodes, s, w = stack.pop()
        
        for node in nodes:
            new_nodes = nodes[:]
            new_nodes.remove(node)
            new_nodes += binary_tree[node]
            new_s = s
            new_w = w
            if info[node] == 0:
                new_s += 1
            else:
                new_w +=1
            
            if new_s <= new_w:
                continue
                
            answer = max(answer, new_s)
            stack.append((new_nodes, new_s, new_w))
        
    return answer