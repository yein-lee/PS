def solution(users, emoticons):
    
    discount_rate = [10, 20, 30, 40]
    emoticon_discount_rates = []
    results = [] # [가입자수, 판매액, index]
    
    dfs(0, len(emoticons), [], emoticon_discount_rates, discount_rate)
    # print(len(emoticon_discount_rates))
    # print(emoticon_discount_rates)
    
    for i, emoticon_discount_rate in enumerate(emoticon_discount_rates):
        results.append([0, 0, i])
        for j, user in enumerate(users):
            user_price = 0
            for k, emoticon_price in enumerate(emoticons):
                if emoticon_discount_rate[k] >= user[0]:
                    user_price += emoticon_price * (1 - emoticon_discount_rate[k] * 0.01)
                    # print("buy", emoticon_discount_rate[k], user[0], emoticon_price, emoticon_price * (1 - emoticon_discount_rate[k] * 0.01), user_price)
            if user_price >= user[1]:
                # 이모티콘 플러스 서비스 가입
                results[-1][0] += 1
            else:
                results[-1][1] += user_price
                    
    results.sort(reverse=True)
    # print(results)
    # print(emoticon_discount_rates[results[0][2]])
    
    return results[0][:2]
                
    
def dfs(t, n, arr, emoticon_discount_rates, discount_rate):
    if len(arr) == n:
        emoticon_discount_rates.append(arr[:])
        return

    for i in range(len(discount_rate)):
        new_arr = arr[:]
        new_arr.append(discount_rate[i])
        dfs(i, n, new_arr, emoticon_discount_rates, discount_rate)

    