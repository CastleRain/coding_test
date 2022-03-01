"""
https://www.acmicpc.net/problem/1676

2 * 5가 몇개인지 세면 된다.

"""

n = int(input())

cnt_2 = 0
cnt_5 = 0

for i in range(1, n+1):
    while True:

        if i % 5 == 0:
            cnt_5 += 1
            i /= 5
        elif i % 2 == 0:
            cnt_2 += 1
            i /= 2
        else:
            break

print(min(cnt_2, cnt_5))

