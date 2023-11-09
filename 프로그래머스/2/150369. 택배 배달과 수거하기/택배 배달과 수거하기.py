def solution(cap, n, deliveries, pickups):
    answer = 0
    
    d_count = []
    p_count = []
    
    c = 0
    init = True
    for i in range(n-1, -1, -1):
        if init and deliveries[i] !=0 :
            d_count.append(i+1)
            
        if deliveries[i] !=0:
            c += deliveries[i]
            init = False
        
        if c == cap:
            c = 0
            init = True
            
        while c > cap:
            c -= cap
            d_count.append(i+1)
            
            
    c = 0
    init = True
    for i in range(n-1, -1, -1):
        if init and pickups[i] !=0:
            p_count.append(i+1)
            
        if pickups[i] !=0:
            c += pickups[i]
            init = False
            
        if c == cap:
            c = 0
            init = True
        
        while c > cap:
            c -= cap
            p_count.append(i+1)
            
            
    if len(d_count) > len(p_count):
        p_count += [0] * (len(d_count) - len(p_count))
    elif len(p_count) > len(d_count):
        d_count += [0] * (len(p_count) - len(d_count))

        
    for i in range(len(p_count)):
        answer += max(p_count[i], d_count[i]) * 2
            
    return answer
