from collections import defaultdict
"""
그룹 단어 체커
https://www.acmicpc.net/problem/1316



"""

n = int(input())
count = 0


for _ in range(n):
    word = input()

    check = 0
    checker = defaultdict(int)

    for w in word:

        # 처음 들어온 글자라면 count를 늘린다.
        if checker[w] == 0:
            checker[w] += 1
        else:
            if prv_word == w:
                checker[w] += 1
            else:
                check+=1
                break

        prv_word = w

    if check != 1:
        count += 1

print(count)