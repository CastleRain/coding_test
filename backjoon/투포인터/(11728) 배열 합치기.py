"""
https://www.acmicpc.net/problem/11728

"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

n_data = []

for i in list(map(int, input().split())):
    n_data.append(i)


for i in list(map(int, input().split())):
    n_data.append(i)

n_data.sort()

for i in range(len(n_data)):
    print(n_data[i], end = " ")