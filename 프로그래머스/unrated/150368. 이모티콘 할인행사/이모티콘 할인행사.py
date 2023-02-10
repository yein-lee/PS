from itertools import product


def solution(users, emoticons):
    m = len(emoticons)
    discount_rates_of_emoticons = list(product([10, 20, 30, 40], repeat=m))

    max_subscriber = 0
    max_sales_of_max_subscriber = 0

    for discount_rate_of_emoticons in discount_rates_of_emoticons:
        entire_sales = 0
        subscriber = 0
        for j in range(len(users)):
            rate, cost = users[j]
            costs_user_purchased = 0
            for i in range(m):
                if discount_rate_of_emoticons[i] >= rate:
                    costs_user_purchased += emoticons[i] * (1 - int(discount_rate_of_emoticons[i]) / 100)
            
            if costs_user_purchased >= cost:
                subscriber += 1
            else:
                entire_sales += costs_user_purchased

        if subscriber > max_subscriber:
            max_subscriber = subscriber
            max_sales_of_max_subscriber = entire_sales
        elif subscriber == max_subscriber:
            if entire_sales > max_sales_of_max_subscriber:
                max_sales_of_max_subscriber = entire_sales

    return [max_subscriber, max_sales_of_max_subscriber]