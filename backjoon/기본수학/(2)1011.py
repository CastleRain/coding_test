"""
Fly me to the Alpha Centauri
https://www.acmicpc.net/problem/1011
"""

n = int(input())

data = []

cnt = 0
sum = 0
for _ in range(n):
    data.append(map(int, input().split()))


for a, b in data:
    test = b-a
    cnt = 0
    sum = 0
    while test > sum:
        cnt+=1
        sum += 2 * cnt

    sum /= 2
    if sum + cnt > test:
        print(cnt * 2 - 1)

    else:
        print(cnt * 2)


