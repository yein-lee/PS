from collections import defaultdict


N = int(input())
words = defaultdict(int)
for _ in range(N):
    word = input()
    for i in range(len(word)):
        words[word[i]] += 10 ** (len(word) - i - 1)

answer = 0
n = 9
sorted_words = {k: v for k, v in sorted(words.items(), key=lambda item: item[1], reverse=True)}
for value in sorted_words.values():
    answer += n*value
    n -= 1

print(answer)
