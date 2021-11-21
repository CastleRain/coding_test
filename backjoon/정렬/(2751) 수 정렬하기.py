"""
수 정렬하기
N <1,000,000

"""

import sys

n = int(sys.stdin.readline())
data = []
for _ in range(n):
    data.append(int(sys.stdin.readline()))

data.sort()
for d in data:
    print(d)