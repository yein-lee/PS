def solution(coin, cards):
    n = len(cards)
    a = [False] * (len(cards) + 1)
    b = [False] * (len(cards) + 1)
    for card in cards[:n // 3]:
        a[card] = True

    i = n // 3
    t = 1
    
    def combo_in_a():
        for j in range(1, n // 2 + 1):
            if a[j] and a[n+1-j]:
                a[j] = False
                a[n+1-j] = False
                return True
        return False
        
    def combo_in_a_and_b():
        for j in range(1, n // 2 + 1):
            if a[j] and b[n+1-j]:
                a[j] = False
                b[n+1-j] = False
                return True
            if a[n+1-j] and b[j]:
                a[n+1-j] = False
                b[j] = False
                return True
        return False
    
    def combo_in_b():
        for j in range(1, n // 2 + 1):
            if b[j] and b[n+1-j]:
                b[j] = False
                b[n+1-j] = False
                return True
        return False
        
    
    while i<len(cards):
        b[cards[i]] = True
        b[cards[i + 1]] = True
        i += 2
        
        if coin >= 0 and combo_in_a():
            pass
        elif coin >= 1 and combo_in_a_and_b():
            coin -= 1
        elif coin >= 2 and combo_in_b():
            coin -= 2
        else:
            break
            
        t += 1
    
    return t


