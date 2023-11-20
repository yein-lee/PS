import math


def solution(n, k):
    num_k = convert_notation(n, k)
    parts = num_k.split('0')
    answer = 0
    for part in parts:
        if len(part) > 0 and is_prime_number(int(part)):
            answer += 1
    return answer


def convert_notation(n, k):
    num_k = list()
    while n != 0:
        num_k.append(n%k)
        n //= k
    return ''.join(map(str, reversed(num_k)))


def is_prime_number(n):
    if n == 1:
        return False
    
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True
    
