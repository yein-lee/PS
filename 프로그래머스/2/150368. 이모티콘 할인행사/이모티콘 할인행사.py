def solution(users, emoticons):
    
    discount_rate = [10, 20, 30, 40]
    discount_rate_comb = []
    results = [] 
    
    dfs(len(emoticons), [], discount_rate_comb, discount_rate)
    
    for comb in discount_rate_comb:
        results.append([0, 0])
        for r, max_total in users:
            total = sum(
                price * (1 - discount/100.0)
                for price, discount in zip(emoticons, comb)
                if discount >= r
            )
            if total >= max_total:
                results[-1][0] += 1
            else:
                results[-1][1] += total
                    
    results.sort(reverse=True)

    return results[0]
                
    
def dfs(n, arr, discount_rate_comb, discount_rate):
    if len(arr) == n:
        discount_rate_comb.append(arr[:])
        return

    for i in range(len(discount_rate)):
        new_arr = arr[:]
        new_arr.append(discount_rate[i])
        dfs(n, new_arr, discount_rate_comb, discount_rate)

    