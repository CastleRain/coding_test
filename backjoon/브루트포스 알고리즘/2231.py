"""
분해합
https://www.acmicpc.net/problem/2231
"""


n = int(input())


data = []
for i in range(n):
    sum = 0
    for j in str(i):

        sum += int(j)
    sum += i


    if sum == n:
        data.append(i)
if len(data) == 0:
    print("0")
else:
    print(min(data))


