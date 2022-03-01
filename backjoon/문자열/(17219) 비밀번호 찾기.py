"""
https://www.acmicpc.net/problem/17219

N : 저장된 사이트 수
M :  비밀번호를 찾으려는 사이트 주소

사이트 주소와 비밀번호는 공백으로 구분

"""

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

data = {}
for _ in range(n):
    a, b = map(str, input().split())
    data[a] = b

for _ in range(m):
    print(data[input().strip()])
