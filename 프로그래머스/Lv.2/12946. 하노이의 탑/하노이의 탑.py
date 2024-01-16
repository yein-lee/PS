def solution(n):
    
    
    def hanoi_tower(n, start=1, end=3):
        aux = 6 - start - end
        if n == 1:
            return [[start, end]]

        return hanoi_tower(n-1, start, aux) + [[start, end]] + hanoi_tower(n-1, aux, end)
    
    answer = hanoi_tower(n, 1, 3)

    return answer