from collections import defaultdict


def solution(sLength, pLength, s, count):
    l, r = 0, pLength-1
    charCount = defaultdict(int)
    for i in range(pLength):
        charCount[s[i]] += 1

    result = 0
    if charCount['A'] >= count[0] and charCount['C'] >= count[1] and charCount['G'] >= count[2] and charCount['T'] >= count[3]:
        result += 1

    for r in range(pLength, sLength):
        charCount[s[r]] += 1
        charCount[s[l]] -= 1
        l += 1
        if charCount['A'] >= count[0] and charCount['C'] >= count[1] and charCount['G'] >= count[2] and charCount['T'] >= count[3]:
            result += 1

    return result


sLength, pLength = map(int, input().split())
s = input()
count = list(map(int, input().split()))
result = solution(sLength, pLength, s, count)
print(result)
