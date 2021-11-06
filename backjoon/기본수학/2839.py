"""
설탕배달
https://www.acmicpc.net/problem/2839
"""

n = int(input())

cnt = 0
while n>0:

    if n % 5==0:
        cnt += n/5
        n = 0
    else:
        cnt += 1
        n -= 3

if n == 0:
    print(int(cnt))
else:
    print("-1")
