def solution(cap, n, deliveries, pickups):
    answer = 0
    
    deliveryAmount = 0
    pickUpAmount = 0
    
    for i in range(n-1, -1, -1):
        deliveryAmount += deliveries[i]
        pickUpAmount += pickups[i]
        
        while deliveryAmount > 0 or pickUpAmount > 0:
            deliveryAmount -= cap
            pickUpAmount -= cap
            answer += (i + 1) * 2
            
    return answer
