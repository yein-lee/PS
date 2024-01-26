def solution():
    N = int(input())
    coins = [tuple(map(int, input().split())) for _ in range(N)]
    total_price = sum(price * count for price, count in coins)

    if total_price % 2 == 1:
        print(0)
        return

    dp = [0 for _ in range(total_price//2+1)]
    dp[0] = 1

    for i in range(N):
        price, count = coins[i]
        if price <= total_price//2:
            for y in range(total_price//2 - price, -1, -1):
                if dp[y] == 1:
                    for j in range(1, count+1):
                        if j * price + y <= total_price // 2:
                            dp[j * price + y] = 1
            if dp[-1] == 1:
                print(1)
                return

    print(0)
    return


for _ in range(3):
    solution()