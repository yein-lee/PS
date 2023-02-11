def solution(cap, n, deliveries, pickups):
    answer = 0

    delivery_stack = []
    pickup_stack = []

    for i, delivery in enumerate(deliveries):
        if delivery > 0:
            delivery_stack.append((i + 1, delivery))

    for i, pickup in enumerate(pickups):
        if pickup > 0:
            pickup_stack.append((i + 1, pickup))

    while delivery_stack or pickup_stack:
        # print(delivery_stack)
        # print(pickup_stack)
        
        if delivery_stack and pickup_stack:
            answer += max(delivery_stack[-1][0], pickup_stack[-1][0]) * 2
            # print(max(delivery_stack[-1][0], pickup_stack[-1][0]), delivery_stack[-1][0], pickup_stack[-1][0])
        elif delivery_stack:
            answer += delivery_stack[-1][0] * 2
            # print("delvery_stack", delivery_stack[-1][0])
        elif pickup_stack:
            answer += pickup_stack[-1][0] *2
            # print("pickup_stack", pickup_stack[-1][0])
        
        delivery_left_count = cap
        pickup_left_count = cap

        while delivery_stack and delivery_left_count != 0:
            delivery_distance, delivery_count = delivery_stack.pop()
            if delivery_count > delivery_left_count:
                delivery_count -= delivery_left_count
                delivery_stack.append((delivery_distance, delivery_count))
                delivery_left_count = 0
            else:
                delivery_left_count -= delivery_count

        while pickup_stack and pickup_left_count != 0:
            pickup_distance, pickup_count = pickup_stack.pop()
            if pickup_count > pickup_left_count:
                pickup_count -= pickup_left_count
                pickup_stack.append((pickup_distance, pickup_count))
                pickup_left_count = 0
            else:
                pickup_left_count -= pickup_count

    return answer
