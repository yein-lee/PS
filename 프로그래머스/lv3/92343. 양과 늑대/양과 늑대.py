def solution(info, edges):
    binary_tree = [[] for _ in range(len(info))]
    for parent, child in edges:
        binary_tree[parent].append(child)

    answer = 0
    
    def dfs(sheep, wolf, nodes_to_search):
        nonlocal answer
        
        if sheep > wolf:
            answer = max(sheep, answer)
        else:
            return
        
        for node in nodes_to_search:
            is_wolf = info[node]
            nodes_to_search_next = nodes_to_search.copy()
            nodes_to_search_next.remove(node)
            nodes_to_search_next.extend(binary_tree[node])
            dfs(sheep + (is_wolf==0), wolf + is_wolf, nodes_to_search_next)
        
    dfs(1, 0, binary_tree[0])
    
    return answer