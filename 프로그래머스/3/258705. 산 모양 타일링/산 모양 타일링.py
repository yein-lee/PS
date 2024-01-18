from collections import deque


def solution(n, tops):
    tiles = [0] * (2*n+1)
    for i, top in enumerate(tops):
        if top == 1:
            tiles[i*2+1] = 1
            
    dp = [0] * (2*n + 1)
    dp[0] = 1 
    if tiles[1] == 1:
        dp[1] = 3
    else:
        dp[1] = 2

    for i in range(2, 2*n + 1):
        if tiles[i] == 1:
            dp[i] = (dp[i-2] + dp[i-1] *2) % 10007
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % 10007
            

    return dp[-1]