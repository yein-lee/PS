def solution(places):
    answer = []
    
    for place in places:
        people = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    people.append((i, j))
                    
        comb = get_distance_combination(0, [], people, [])
        answer.append(1 if is_under_control(place, comb)==True else 0)
                        
    return answer


def get_distance_combination(i, cur, arr, comb):
    if len(cur) == 2:
        comb.append(cur)
        return comb
    
    for j in range(i, len(arr)):
        comb = get_distance_combination(j+1, cur[:] + [arr[j]], arr, comb)
        
    return comb


def is_under_control(place, comb):
    for coor1, coor2 in comb:
        r1, c1 = coor1
        r2, c2 = coor2
        d = get_manhaton_distance(r1, c1, r2, c2)
        if d == 1:
            return False
        elif d == 2:
            if r2 == r1 + 2 and place[r1+1][c1] != 'X':
                return False
            elif r2 == r1 + 1 and c2 == c1 - 1 and (place[r1+1][c1] != 'X' or place[r1][c1-1] != 'X'):
                return False
            elif c2 == c1 - 2 and place[r1][c1-1] != 'X':
                return False
            elif r2 == r1 - 1 and c2 == c1 - 1 and (place[r1][c1-1] != 'X' or place[r1-1][c1] != 'X'):
                return False
            elif r2 == r1 - 2 and place[r1-1][c1] != 'X':
                return False
            elif r2 == r1 - 1 and c2 == c1 + 1 and (place[r1-1][c1] != 'X' or place[r1][c1+1] != 'X'):
                return False
            elif c2 == c1 + 2 and place[r1][c1+1] != 'X':
                return False
            elif r2 == r1 + 1 and c2 == c1 + 1 and (place[r1+1][c1] != 'X' or place[r1][c1+1] != 'X'):
                return False
    return True


def get_manhaton_distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)