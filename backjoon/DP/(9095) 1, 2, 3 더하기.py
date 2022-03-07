"""
https://www.acmicpc.net/problem/9095

"""

d = [0]*10

n = int(input())

data = []
for _ in range(n):
    data.append(int(input()))

d[0] = 1
d[1] = 2
d[2] = 4


for i in range(10):
    if d[i] != 0:
        continue

    d[i] = d[i-1] + d[i-2] + d[i-3]

for i in data:
    print(d[i-1])