def solution(h1, m1, s1, h2, m2, s2):
    t1 = h1 * 60 * 60 + m1 * 60 + s1
    t2 = h2 * 60 * 60 + m2 * 60 + s2
    
    H_S = []
    i = 0
    while True:
        if ((120 * 360) / 719) * i >= 24* 60 * 60:
            break
        H_S.append(((120 * 360) / 719) * i)
        i += 1
    
    M_S = []
    i = 0
    while True:
        if (3600/59) * i >= 24* 60 * 60:
            break
        M_S.append((3600/59) * i)
        i += 1
    
    answer = set()
    for s in H_S:
        if t1 <= s <= t2:
            answer.add(s)

    for s in M_S:
        if t1 <= s <= t2:
            answer.add(s)
            
    return len(answer)