def solution(queue1, queue2):
    q = queue1 + queue2
    n = len(queue1)
    total = sum(q)
    if total % 2 != 0:
        return -1
    
    half = total // 2
    
    c1 = 0
    p1, p2 = 0, n-1
    s = sum(q[p1:p2+1])
    
    while True:
        if s < half:
            p2 += 1
            if p2 == n*2:
                c1 = -1
                break
            s += q[p2]
        elif s > total // 2:
            s -= q[p1]
            p1 += 1
            if p1 == n*2:
                c1 = -1
                break
        else:
            break
        c1 += 1
    
    c2 = 0
    q = queue2 + queue1
    p1, p2 = 0, n-1
    s = sum(q[p1:p2+1])
    while True:
        if s < total // 2:
            p2 += 1
            if p2 == n*2:
                c2 = -1
                break
            s += q[p2]
        elif s > total // 2:
            s -= q[p1]
            p1 += 1
            if p1 == n*2:
                c2 = -1
                break
        else:
            break
        c2 += 1
    
    answer = 0
    if c1 == -1 and c2 == -1:
        answer = -1
    elif c1 == -1 or c2 == -1:
        answer = max(c1, c2)
    else:
        answer = min(c1, c2)
    return answer